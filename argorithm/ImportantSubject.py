import csv
import re
import networkx as nx

G = nx.DiGraph()

Person_csv = open('Chương trình 1303 - Kỹ thuật Máy tính 2018 cho sinh viên 20183694 Bùi Đức Chế.csv', 'r', encoding="utf-8-sig")
Person_data = csv.DictReader(Person_csv)
EDUCATION_PROGRAMME_NAME = Person_csv.name
EDUCATION_PROGRAMME_COURSES = []


for perCourse in Person_data:
    # if perCourse['Điểm chữ'] is None or perCourse['Điểm chữ'] == "F" or perCourse['Điểm chữ'] == "I":
    EDUCATION_PROGRAMME_COURSES.append(perCourse['Mã HP'])

csvfile = open('CourseListdata.csv', 'r', encoding="utf-8-sig")
'''File dữ liệu đầu vào, kết quả của quá trình crawl dữ liệu trang sis'''
# csvfile = open("E:\StProjects/2020-2021\BuiDucChe_CrawlVaVeCayPhuThuocHocPhan\sources/assets/CourseListdata.csv", 'r',encoding="utf-8")

reader = csv.DictReader(csvfile)

standardizedCourses = [];
''' Danh sách đầy đủ các course với thông tin đã được chuẩn hoá.'''

# Bố trí lại thông tin phụ thuộc
for myCourse in reader:
    dk = str(myCourse['Học phần điều kiện']);
    dependency = dk.replace("*", "").replace("=", "").replace(" ", "").replace("!", "")

    myCourse['X'] = myCourse['Mã học phần']  # Mã học phần chính, trùng lặp dữ liệu để tiện cho thuật toán tìm quan hệ
    myCourse['Y'] = dependency  # Mã học phần điều kiện, trùng lặp dữ liệu để tiện cho thuật toán tìm quan hệ
    # if len(dependency) > 60:
    #    print(myCourse)
    standardizedCourses.append(myCourse)
for myCourse in standardizedCourses:
    if not myCourse['X'] in EDUCATION_PROGRAMME_COURSES:
        continue
    a = re.split('/|, |,|\)|\(|\*', myCourse['Y'])
    for i in a:
        if i != '' and i in EDUCATION_PROGRAMME_COURSES: G.add_edge(myCourse['X'], i)

# Tính toán In-degree Centrality của tất cả các node trong đồ thị
in_degree_centrality = nx.in_degree_centrality(G)

# Sắp xếp các node theo thứ tự giảm dần của In-degree Centrality
sorted_in_degree_centrality = sorted(in_degree_centrality.items(), key=lambda x: x[1], reverse=True)
print(sorted_in_degree_centrality)

