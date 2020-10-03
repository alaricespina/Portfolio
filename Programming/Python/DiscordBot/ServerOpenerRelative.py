from selenium import webdriver
from selenium.webdriver.common.keys import Keys #simple clicking thing
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

Path = "Dependencies\chromedriver.exe"
driver = webdriver.Chrome(Path) 

aternosuser = "BigPeni69"
aternospass = "hulkpenisbig69"

driver.get("https://aternos.org/:en/")
#just prints the title of the webpage
title = driver.title
print(title)

#Assuming you are on the signup page
link = driver.find_element_by_link_text("Play")
link.click()

#Wait for the id and password
try:
    #Check if logged in, if no this stuffs should be found
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"user")))
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"password")))
    
except:
    logoutelement = driver.find_element_by_class_name("logout")
    logoutelement.click()
    #If it is logged in, will logout the account first
    print("No sht found")
     

print("Hatdog, I Have succesfully found the user and pass")  

#fill up the username and password
userelement = driver.find_element_by_id("user")
userelement.send_keys(aternosuser)
passelement = driver.find_element_by_id("password")
passelement.send_keys(aternospass)

#Click on the login button
loginelement = driver.find_element_by_id('login')
loginelement.click()

#Check if server is already online
try:
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,"server-title")))
except:
    print("\nServer is already online u bitch\n")

print("\nServer is currently offline\n\nTurning on. . .")

#Click on server
serverelement = driver.find_element_by_class_name("server-title")
serverelement.click()

#Wait for status to load
try:
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,"server-status")))
except:
    print("\nCannot Find a server\n")

while True:
    statuselement = driver.find_element_by_class_name("statuslabel-label")
    statustxt = statuselement.text #String
    if statustxt == "Offline":
        startbutton = driver.find_element_by_id("start")
        startbutton.click()
        print("\nServer is now Starting\n")

    if statustxt == "Online":
        print("\nServer is now online\n")
        driver.quit()
        break
    


#driver.quit() #close 


