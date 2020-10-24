#selenium version of slideshow
#22/40
from selenium import webdriver
from selenium.webdriver.common.keys import Keys #simple clicking thing
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

Path = "chromedriver.exe"
driver = webdriver.Chrome(Path)

slideshowlink = "https://jungleofferwall.com/offerwall/5/217537947?type=nightfallnews"
def stap():
    time.sleep(3)
driver.get(slideshowlink)

n = 0 
while True:
    print(f"Current loop {n}")
    #Bot Checker
    try:
        checker = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.ID,"survey-scroll-text"))) 
        point = driver.find_elements_by_xpath("//*[@class='ob-unit' or @class='ob-rec-source']")
        point.click()        
    except:
        print("No Bot Checkers")

    print("Sleeping")
    time.sleep(10)
    print("Sleep Done")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight-100);")
    stap()
    element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID,"nextButton"))) 
    stap()
    element.click()
    stap()
    print("Clicked")
    stap()
