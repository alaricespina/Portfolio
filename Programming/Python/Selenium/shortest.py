from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import random
import time

options = webdriver.ChromeOptions()
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--headless')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
waitdelay = 10 #in seconds

def findByLinkText(LT):
    return driver.find_element_by_link_text(LT)

def findByID(Id):
    return driver.find_element_by_id(Id)

def findByClass(Classname):
    return driver.find_element_by_class_name(Classname)

def waitForLinkText(LT):
    try:
        WebDriverWait(driver, waitdelay).until(EC.visibility_of_element_located((By.LINK_TEXT,LT)))
    except:
        print("Error")

def waitForID(Id):
    try:
       WebDriverWait(driver, waitdelay).until(EC.visibility_of_element_located((By.ID,Id)))
    except:
        print("Error")

def waitForClass(Classname):
    try:
       WebDriverWait(driver, waitdelay).until(EC.visibility_of_element_located((By.CLASS_NAME,Classname)))
    except:
        print("Error")



linktxt = open("Hatdog.txt")
links = [i for i in linktxt]
for x in links:
    print(x)

linktxt.close()
print(links)

CLI = random.randint(0,len(links)-1)
target = links[CLI]
print(target)

driver.get(target)
print("Sleeping for 10")
time.sleep(10)
print("Sleep done")
try:
    WebDriverWait(driver, waitdelay).until(EC.visibility_of_element_located((By.ID,"rc-imageselect")))
    driver.close()
except:
    print("No Captcha")

waitForID("skip_button")
enter = findByID("skip_button")
try:
    enter.click()
except:
    print("Thingy not clickable")

print("Enter Clicked")

driver.close()
driver.quit()