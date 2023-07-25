from numpy import NAN, mod
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import html2text
import pandas as pd
import os

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# create a url variable that is the website link that needs to crawl
BASE_URL = 'https://ctt-sis.hust.edu.vn/Students/StudentProgram.aspx'  # 20167995
LOGIN_USERNAME = "20167995"
LOGIN_PASSWORD = "20167995"

# Thư mục chứa kết quả
COURSE_COLLECTION_FOLDER = ""

# Số lượng course trong mỗi trang thông tin.
COURSE_PER_PAGE = 15

# Select Webbrowser. 1 =Firefox, 2 = Chrome, 3 = Edge
WebBrowserSelector = 2

# Khai bao bien browser điều khiển quá trình crawl
browser = NAN
browser_actions = NAN


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Crawl():

    def autologin(browser,Username, Password, ExpectedTitle=""):
        """_summary_
            Phụ trách nhập thông tin tài khoản đăng nhập
        Args:
            Username (string): tên tài khoản
            Password (string): mật khẩu
            ExpectedTitle (string): một phần trong tiêu đề của trang web sau đăng nhập, nhằm xác định việc đăng nhập là thành công.
        """
        browser_actions = ActionChains(browser);

        # ---------------------------------------------------
        # ---   ĐĂNG NHẬP
        # ---------------------------------------------------

        # Nhập username
        browser.find_element(By.ID, "ctl00_ctl00_contentPane_MainPanel_MainContent_tbUserName_I").send_keys(Username)

        # Nhập mật khẩu. 
        # Lưu ý: phải dùng tương tác bàn phím vì không tìm được đối tượng ctl00_ctl00_contentPane_MainPanel_MainContent_tbPassword_I 
        if (Password != "") and (Password != NAN):
            browser_actions.send_keys(Keys.TAB)
            browser_actions.send_keys(Password)
            browser_actions.send_keys(Keys.PAGE_DOWN)
            browser_actions.send_keys(Keys.TAB)
            browser_actions.send_keys(Keys.TAB)
        else:
            print("Please type the password")

        # Nhập captcha
        Captcha = input("Enter the captcha: ")
        print(Captcha)
        browser_actions.send_keys(Captcha)
        browser_actions.send_keys(Keys.ENTER)
        browser_actions.perform()
        print("current_url", browser.current_url)

        # browser.find_element(By.ID, "cLogIn1_bt_cLogIn_CD").send_keys(Keys.ENTER)
        try:
            elem = WebDriverWait(browser, 30).until(
                # Đợi cho tới khi title của trình duyệt đổi tên mới. Đã chạy tốt
                EC.title_contains(ExpectedTitle)
                # Đợi cho tới khi một handle được tìm thấy. Đã chạy tốt
                # EC.presence_of_element_located((By.ID, "ctl00_ctl00_contentPane_MainPanel_MainContent_gvCourses_DXPagerBottom_PBN")) #This is a dummy element
            )
            print("Login successfully.")
        except:
            print("Login process is out of time. Please do it again.")
            browser.quit()
        print("Login finished.")
        # -----------------------------------------------------------------------------------------------------

    # Thử nghiệm:
    #    Ở trang course-list: trên browser, mở console, chỉ cần gọi trực tiếp hàm
    #         ASPx.GVPagerOnClick('ctl00_ctl00_contentPane_MainPanel_MainContent_gvCourses','PN479')
    #    và thay PN479 bằng PN334, là sẽ gọi được tới đúng từng trang.
    # -----------------------------------------------------------------------------------------------------
    def crawlStudentProgramdata(browser):

        datacrawl = []
        # Mở chương trình đào tạo sinh viên
        MainPanelBotton = browser.find_element(By.CSS_SELECTOR,'#ctl00_ctl00_contentPane_MainPanel_MainContent_btShowProgramCourse')
        MainPanelBotton.click()
        # Xác định thông tin crawl
        TitlePanel = browser.find_element(By.CSS_SELECTOR,'.dxgvTitlePanel')
        print(TitlePanel.text)
        # Crawl thông tin môn học của sinh viên
        Programdata = browser.find_elements(By.CSS_SELECTOR,'[id^=ctl00_ctl00_contentPane_MainPanel_MainContent_ProgramCoursePanel_gvStudentProgram_DXDataRow]')

        courseIndex = 0
        for Studentdata in Programdata:

            data = Studentdata.find_elements(By.CSS_SELECTOR, '.dxgv')

            # Kiểm tra checkBox của học phần bắt buộc
            checkBox = Studentdata.find_element(By.CSS_SELECTOR,'.dxICheckBox')
            class_value = checkBox.get_attribute("class")
            # print('dxWeb_edtCheckBoxChecked' in class_value)

            # Tạo cấu trúc lưu trữ
            dataprogram = {'STT': courseIndex,
                          'Mã HP': data[2].text,
                          'Tên HP': data[3].text,
                          'Kỳ học': data[4].text,
                          'Bắt buộc': 'dxWeb_edtCheckBoxChecked' in class_value,
                          'TC ĐT': data[6].text,
                          'TC học': data[7].text,
                          'Mã HP học': data[8].text,
                          'Ghi chú loại HP': data[9].text,
                          'Điểm chữ': data[10].text,
                          'Điểm số': data[11].text,
                          'Viện/Khoa': data[12].text
                          }
            print(Studentdata.text)
            courseIndex = courseIndex + 1
            datacrawl.append(dataprogram)
        # Ghi du lieu
        # print(datacrawl)
        df = pd.DataFrame(datacrawl)
        df.to_csv(f'{TitlePanel.text}.csv')
        # dong trinh duyet
