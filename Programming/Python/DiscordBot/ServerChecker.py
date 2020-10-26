from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager



def ServerOpen():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    waitdelay = 10 #in seconds
    #Account
    aternosuser = "BigPeni69"
    aternospass = "hulkpenisbig69"
    driver.get("https://aternos.org/:en/") #URL For Aternos Server

    def findByLinkText(LT):
        return driver.find_element_by_link_text(LT)

    def findByID(Id):
        return driver.find_element_by_id(Id)

    def findByClass(Classname):
        return driver.find_element_by_class_name(Classname)

    def waitForLinkText(LT):
        try:
            element = WebDriverWait(driver, waitdelay).until(EC.presence_of_element_located((By.LINK_TEXT,LT)))
        except:
            print("Error")

    def waitForID(Id):
        try:
            element = WebDriverWait(driver, waitdelay).until(EC.presence_of_element_located((By.ID,Id)))
        except:
            print("Error")

    def waitForClass(Classname):
        try:
            element = WebDriverWait(driver, waitdelay).until(EC.presence_of_element_located((By.CLASS_NAME,Classname)))
        except:
            print("Error")

    #Assuming you are on the signup page
    waitForLinkText("Play")
    link = findByLinkText("Play")
    link.click()

    try: #In Case you were already logged in
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"user")))
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"password")))
        
    except: #This will log you out
        logoutelement = driver.find_element_by_class_name("logout")
        logoutelement.click()

    #fill up the username and password
    userelement = findByID("user")
    userelement.send_keys(aternosuser)
    passelement = findByID("password")
    passelement.send_keys(aternospass)

    #Click on the login button
    loginelement = findByID('login')
    loginelement.click()

    #Wait for the server list to load
    waitForClass("server-title")

    #Click on server
    serverelement = findByClass("server-title")
    serverelement.click()

    #Wait for status to load
    waitForClass("statuslabel-label")

    while True:
        statuselement = findByClass("statuslabel-label")
        statustxt = statuselement.text #String
        print(statustxt)
        if statustxt == "Offline":
            waitForID("start")
            startbutton = findByID("start")
            startbutton.click()

            try: #IF an Alert box opens, closes it
                element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,"alert-close")))
                alertbutton = driver.find_element_by_class_name("alert-close")
                alertbutton.click()
            except:
                print("No Alerts ok")
            
            print("\nServer is now Starting\n")


        if statustxt == "Online":
            print("\nServer is now online\n")
            driver.quit()
            break

        if statustxt == "Waiting in queue":
            try: #Still on loop, will wait until confirm button is visible
                element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID,"confirm")))
                confirmbutton = driver.find_element_by_id("confirm")
                confirmbutton.click()
                break
            except:
                print("Its still Waiting on Queue")

    driver.quit() #close 

