
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

browser = webdriver.Firefox()

browser.get('https://portal.lanis-system.de/?i=6110')


action = ActionChains(browser)
wait = WebDriverWait(browser, 10)  # Adjust the timeout as needed


# user data               
kurzel = "stk" # Kürzel PS = offline kürzel / STK 27775
pw = "27775" # later on should be importet from csv file library
timeoutLen = 20 # 1 = 30s --> 1-4 Iterationen um den Account zu sperren.


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
     
def invadeN():
   browser.get('https://start.schulportal.hessen.de/nachrichten.php')
   wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

   newConv = browser.find_element(By.ID, 'new')
   print(newConv)
   time.sleep(2)
   browser.find_element(By.ID,'new').click()  
   parentDiv= browser.find_elements(By.CLASS_NAME, 'select2-search__field')
   print(parentDiv)
   inputField = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input.select2-search__field')))
   print(inputField)
   
   letterS = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

   for x in letterS:
      letter1 = x
      for i in letterS:
       letter2 = i
       inputLetterAre = str(letter1)+str(letter2)
       

       inputField.clear()
       inputField.send_keys(inputLetterAre)
       time.sleep(2)
       
       try:
           results = browser.find_element(By.ID,'select2-to-results')
           li_elements = results.find_elements(By.TAG_NAME, 'li')
           print(li_elements)
           #time.sleep(2)
   

           csv_filename = "li_elements2.csv"

           with open(csv_filename, mode='a', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
    
                # Write a header row (optional)
                csv_writer.writerow(['header'])
                for li_elements in li_elements:
                 text = li_elements.text
                 csv_writer.writerow([text])
       except:
          print("no name found under the letter combo" + str(inputLetterAre))
        
         

   

    
      

   


def execute():
    login() 
    time.sleep(2)
    invadeN()
    
execute()
    
  