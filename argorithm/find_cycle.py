import pandas as pd
import re
import networkx as nx
import logging
import datetime
from graphviz import Digraph

filelog = 'find_cycle' + datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S.log")
logging.basicConfig(level=logging.WARNING, filename=filelog, filemode='w', format='%(asctime)s - %(levelname)s - %(message)s')
logging.basicConfig(level=logging.INFO, filename=filelog, filemode='w', format='%(asctime)s - %(levelname)s - %(message)s')

#Load dữ liệu học phần
data = pd.read_csv('CourseListdata.csv')
# data[['id', 'Mã học phần']]

# Lấy thành phần để xây dựng đồ thị
course_relationship=data[['Mã học phần','Học phần điều kiện']].rename({'Mã học phần': 'X', 'Học phần điều kiện': 'Y'}, axis=1)
# print("Tổng số học phần:")
# print(len(course_relationship))
graph=course_relationship[~course_relationship.Y.isnull()]
# f= open("DK.txt","w")

#Danh sách các cạnh
setedge=set()
for index, row in graph.iterrows():
    # f.write(row['Y']+"\n")
    a=re.split('/|, |,|\)|\(|\*', row['Y'])
    for i in a:
        if i !='': setedge.add(row['X']+' '+i)

dot = nx.DiGraph(comment='Course')
dot.format='png'
for edge in setedge:
    e=edge.split(' ')
    dot.add_edge(e[0],e[1], label='')

# Find cycles using Tarjan's algorithm
cycles = list(nx.simple_cycles(dot))

# Print the cycles
if len(cycles) == 0:
    logging.info('No cycles found.')
else:
    logging.warning('Cycles found:')
    for cycle in cycles:
        logging.warning(cycle)
# dot.render('test-output/allcourse', view=False)
dot.clear()
