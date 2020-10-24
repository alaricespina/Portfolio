from selenium import webdriver
from selenium.webdriver.common.keys import Keys #simple clicking thing
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

website = "https://miningph.com/wallet"
user = "alaricsespina@gmail.com"
password = "Alaric828"
Path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(Path) 
driver.get(website)

#Wait for the login details to appear and click the button
while True:
    try:
        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID,"email")))
        break
    except:
        print("Place to put login details")

emailinput = driver.find_element_by_id("email")
passwordinput = driver.find_element_by_id("password")
emailinput.send_keys(user)
passwordinput.send_keys(password)
passwordinput.send_keys(Keys.RETURN)
print("Sleep for 4 seconds")
time.sleep(4)
print("Sleep done")

n = 0 #number of loops

#mining proper
while True:
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)

    #Wait for navbar to appear
    while True:
        try:
            element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME,"navbar-toggler-icon")))
            print(f"{n}:Navigation Bar has been found")
            break
        except:
            print(f"{n}:No Navbar")

    #Click on the navigation bar
    navbtn = driver.find_element_by_class_name("navbar-toggler-icon")
    navbtn.click()

    #Wait for Mining Button to appear
    while True:
        try:
            element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT,"Mining")))
            print(f"{n}:Mining Link Found")
            break
        except:
            print(f"{n}No Mining Option")

    #Click on the Mining Option
    miningbtn = driver.find_element_by_link_text("Mining")
    miningbtn.click()

    print("Sleep for 10 seconds")
    time.sleep(10)
    print("Done sleeping")

    #Click on the start mining thing
    while True:
        try:
            element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//////a[@href="'https://miningph.com/miner?e=1618178'"]")))
            print(f"{n}Mining Button Found")
            break
        except:
            print(f"{n}No Start Mining Option")

    startminingbtns = driver.find_element_by_xpath("//////a[@href="'https://miningph.com/miner?e=1618178'"]")
    startminingbtns.click()
    print(f"{n} | {n}th loop has been completed")
    n += 1


