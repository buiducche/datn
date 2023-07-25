import logging
import datetime
import os
import csv
# Thư mục chứa file đâu vào
COURSE_COLLECTION_FOLDER = "assets"
'''Thư mục chứa file đâu vào'''

# Cơ sở dữ liệu của các học phần, được thu thập từ trang ctt-sis
COURSE_LIST_FILE = 'CourseListdata.csv'
'''Cơ sở dữ liệu của các học phần, được thu thập từ trang ctt-sis'''

# Thư mục chứa file ảnh đầu ra
OUTPUT_FOLDER = COURSE_COLLECTION_FOLDER + "/graph0"
'''Thư mục chứa file ảnh đầu ra'''
#Chuyển đổi đường dẫn tương đối thành tuyệt đối
COURSE_COLLECTION_FOLDER = os.getcwd() + '/../' + COURSE_COLLECTION_FOLDER
OUTPUT_FOLDER = os.getcwd() + '/../' +  OUTPUT_FOLDER



# logging file
filelog = 'transitive_reduction' + datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S.log")
logging.basicConfig(level=logging.WARNING, filename=filelog, filemode='w', format='%(asctime)s - %(levelname)s - %(message)s')
logging.basicConfig(level=logging.INFO, filename=filelog, filemode='w', format='%(asctime)s - %(levelname)s - %(message)s')

# Define a function to parse a .dot file and return a list of edges
def parse_dot_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    edges = []
    for line in lines:
        line = line.strip()
        if line.startswith(('digraph', '}')):
            continue
        if line.endswith(';'):
            line = line[:-1]
        if '->' in line:
            src, dst = line.split('->')
            src = src.strip()
            dst = dst.strip().split("\t")[0].split(" ")[0]
            edges.append((src, dst))
    return edges
def logging_diff(before_tred,after_tred):
    # Parse the first file
    edges1 = parse_dot_file(before_tred)
    # Parse the second file
    edges2 = parse_dot_file(after_tred)
    removed_edges = list(set(edges1) - set(edges2))
    print(removed_edges)
    if len(removed_edges) > 0 :
        logging.warning("Have tred in " + after_tred + " " + str(removed_edges))
    pass
# =====================Main=======================
csvfile = open('CourseListdata.csv', 'r',encoding="utf-8-sig")
'''File dữ liệu đầu vào, kết quả của quá trình crawl dữ liệu trang sis'''
reader = csv.DictReader(csvfile)
for myCourse in reader:
    courseId = myCourse['Mã học phần']
    before_tred = OUTPUT_FOLDER + '/' + courseId + 'tmp'
    after_tred = OUTPUT_FOLDER + '/' + courseId
    try:
        logging_diff(before_tred,after_tred)
    except:
        print("error find different in course " + courseId )

# courseId = "CH3306"
# before_tred = OUTPUT_FOLDER + '/' + courseId + 'tmp'
# after_tred = OUTPUT_FOLDER + '/' + courseId
# logging_diff(before_tred,after_tred)