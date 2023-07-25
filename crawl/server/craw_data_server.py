from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pyvirtualdisplay import Display 
from PIL import Image
from io import BytesIO
from crawl_personalsis import Crawl
# import subprocess
import time

DRIVER_LOCATION = "/usr/bin/chromedriver"
BINARY_LOCATION = "/usr/bin/google-chrome"

LOGIN_USERNAME = "20167995"
LOGIN_PASSWORD = "20167995"

DISPLAY_VISIBLE = 0
DISPLAY_WIDTH = 1920
DISPLAY_HEIGHT = 1080

# start display 
display = Display(visible=DISPLAY_VISIBLE, size=(DISPLAY_WIDTH, DISPLAY_HEIGHT))
display.start()
# subprocess.call(['xrandr', '-s', '1920x1080'])

# start selenium
options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")  # Cho phép chạy chrome với tk root
options.add_argument("--headless")    # Không hiển thị UI
options.add_argument('--disable-dev-shm-usage') # Tránh bị crashed trang do shm nhỏ
options.add_argument("start-maximized")
options.binary_location = BINARY_LOCATION

driver = webdriver.Chrome(executable_path=DRIVER_LOCATION, options=options)

# Login page
driver.get("https://ctt-sis.hust.edu.vn/pub/CourseLists.aspx")
print("current_url", driver.current_url)
title=driver.title
print("title: ", title)

# Scroll down the page by 500 pixels
driver.execute_script("window.scrollBy(0, 500);")

# Wait for the page to load after scrolling
time.sleep(1)

# take a screenshot
# filename = f"{title}.png"
# driver.save_screenshot(filename)

# Get the position and size of the element to capture
element = driver.find_element(By.XPATH, '//*[@id="ctl00_ctl00_contentPane_MainPanel_MainContent_ASPxCaptcha1_IMG"]')
location = element.location
size = element.size

# Calculate the coordinates of the element's bounding box
left = location['x']
top = location['y']
right = location['x'] + size['width']
bottom = location['y'] + size['height']

# Capture a screenshot of the element
screenshot = driver.get_screenshot_as_png()
driver.save_screenshot('test.png')
image = Image.open(BytesIO(screenshot)).crop((left, 186 , right, 266))

# Save the image to a file
image.save("captcha.png")

# Resize the image to fit the terminal width
terminal_width = 80
aspect_ratio = image.width / image.height
terminal_height = int(terminal_width / aspect_ratio)
image = image.resize((terminal_width, terminal_height))

# Convert the image to ASCII art
ascii_chars = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
pixels = image.convert("L").getdata()
ascii_art = "".join([ascii_chars[pixel // 25] for pixel in pixels])

# Display the ASCII art in the terminal
print("\033[1;32m" + ascii_art + "\033[0m")


# 2.2 take a screenshot
# time.sleep(5)
# filename = f"{title}.png"
# driver.save_screenshot(filename)

# Crawl data
Crawl.autologin(driver,LOGIN_USERNAME, LOGIN_PASSWORD, "Courses List")
Crawl.crawldata(driver)

# close browser and quit driver
driver.close()
driver.quit()
display.stop()