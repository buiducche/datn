# Course Dependency

## Overview

A website and webapi show the dependency tree of courses, help students choose which course need to be accomplished early and arrange their learning plan.

## How to run

- Step 1: crawling. It takes about 250 minutes.

```dos
    python ./crawl/local/crawl_personalsis.py
    python ./crawl/local/Crawl_StudentProgram.py
    
    Output:../assets/CourseListdata.csv
           ../assets/{MSSV}.csv
```

- Step 2: generate dependency graphs
    python ./crawl/argorithm/gentree.py
    python ./crawl/argorithm/gentree_personal.py
    
    Output:../assets/graph0/*
           ../assets/{MSSV}.png
- Step 3: run web 
    read ./project/README.md

## Structure of the Source Folder
```
* Thư mục **argorithm** chứa code phân tính dữ liệu crawl và code sinh cây phụ thuộc
* Thư mục **project** chứa code web server 
* Thư mục **crawl** chứa code crawl data dành cho môi trường máy cá nhân và server
* API test:
* http://sinno.soict.ai:37080/api
