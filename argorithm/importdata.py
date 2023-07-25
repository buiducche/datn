import requests
import csv
import json

# API endpoint
url = 'http://localhost:3000/course'
i=0
# Open the CSV file
with open('CourseListdata.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        jsondata = json.dumps({
                'maHocPhan': row['Mã học phần'],
                'tenHocPhan': row['Tên học phần'],
                'thoiLuong': row['Thời lượng'],
                'soTinChi': float(row['Số tín chỉ']),
                'tinChiHocPhi': row['TC học phí'],
                'trongSo': float(row['Trọng số']),
                'hocPhanDieuKien': row['Học phần điều kiện'],
                'tenTiengAnh': row['Tên tiếng anh'],
                'vienQuanLy': row['Viện Quản lý'],
                'mucTieu': row['Mục tiêu'],
                'noiDung': row['Nội dung']})
        # Make a POST request to the API with the course data
        response = requests.post(url, data=jsondata, headers={'Content-Type': 'application/json'})
        # print(jsondata)
        # Check the response status code
        print(i)
        i+=1
        if response.status_code > 201:

            print(jsondata)
            print(f'insert course {row["Mã học phần"]}  {response.status_code}')
