import os
import time
import requests
import json
import pprint
import datetime as datetime
from browsermobproxy import Server
from selenium import webdriver #driver for the code
from selenium.webdriver.common.keys import Keys # to return keystrokes 
from selenium.webdriver.chrome.options import Options # for options such as headless
from selenium.webdriver.common.by import By #what to except by: ie ID, Class, etc. 
from selenium.webdriver.support.ui import WebDriverWait #used to tell selenium to wait
from selenium.webdriver.support import expected_conditions as EC #used to tell selenium what to wait for an expected condition like an ID appearing or class. 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import WebDriverException

#start proxy server
server = Server("C:\\python_sandbox_starter\\browsermob-proxy-2.1.4\\bin\\browsermob-proxy.bat")
server.start()
proxy = server.create_proxy()

#set arguments 
caps = DesiredCapabilities.CHROME
caps['goog:loggingPrefs'] = {'performance': 'ALL'}
caps['acceptSslCerts'] = True
caps['acceptInsecureCerts'] = True

chrome_options = Options()
# chrome_options.add_argument('--headless')
chrome_options.add_argument("--proxy-server={0}".format(proxy.proxy))
#driver configuration
driver = webdriver.Remote(command_executor='http://127.0.0.1:9515', desired_capabilities=caps, options=chrome_options)
driver.get("https://www2.kickassanime.rs")
#har (HTTP archive file) creation, har is a JSON formatted archive file format
proxy.new_har(driver,options={'captureHeaders':True, 'captureContent':True, 'captureBinaryContent':True})

#file to append new video to
filename = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")+'.mpeg'


#List of anime to check for
anime = ["Boku no Hero Academia Season 5", "World Trigger Season 2"]

#Creates a list of episodes from the main-video-list element and searches for anime on the list.

def checkdriver():
   try:
      driver.title
      return True
   except (WebDriverException):
      return False
try:
    element = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.ID, "main-video-list"))
    )
    
    element = ((element.text).split("\n"))
    for e in element:
       if e in anime:
          print(f"Found: {e}")

except:
   driver.quit()
 
#Searches for Anime and clicks it, then finds the episodes asked for (episode 1 as test for now)
try:
   link = driver.find_element_by_link_text("World Trigger Season 2")
   link.send_keys(Keys.RETURN)
   element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "main")))
   element = (element.text).split("\n")
   print(element)
   for i in element:
      if i == "Episode 01":
         # print("Found Episode")
         # link = driver.find_elements_by_link_text(i)
         # print(i)
         time.sleep(2)
         link = WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.LINK_TEXT, i)))
         link.send_keys(Keys.RETURN)
         WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//iframe[@class="embed-responsive-item"]')))
         iframe1 = driver.find_element_by_xpath('//iframe[@class="embed-responsive-item"]')
         driver.switch_to.frame(iframe1)
         print("Inside iframe1")
         time.sleep(4)
         iframe2 = driver.find_element_by_xpath('/html/body/div/iframe')
         driver.switch_to.frame(iframe2)
         print("Inside iframe2")
         driver.implicitly_wait(time_to_wait=2)
         iframe3 = driver.find_element_by_xpath('/html/body/iframe')
         driver.switch_to.frame(iframe3)
         print("Inside iframe3")
         time.sleep(2)
         button = driver.find_element_by_xpath('//*[@id="player"]/button')
         print("Play button selected as 'button'")
         button.send_keys(Keys.RETURN)
         print("Play button pressed")
         

finally:
   print("Starting .ts capture")
   


#runs loop to grab .ts packets and write/append them to a single file for viewing
fetched = []
while checkdriver() == True:
   for ent in proxy.har['log']['entries']:
      _url = ent['request']['url']
      _response = ent['response']
      
    #makes sure it hasn't already downloaded .ts 
      if _url in fetched:
         continue
      if _url.endswith('VA') or _url.endswith('.ts'):
        #check if this url had a valid response, if not, ignore it
         if 'text' not in _response['content'].keys() or not _response['content']['text']:
            continue
         print(_url+'\n')
         r1 = requests.get(_url, stream=True)
         if(r1.status_code == 200 or r1.status_code == 206):

            # re-open output file to append new video
            with open(filename,'ab') as f:
                data = b''
                for chunk in r1.iter_content(chunk_size=1024):
                    if(chunk):
                        data += chunk
                f.write(data)
                fetched.append(_url)
         else:
            print("Received unexpected status code {}".format(r1.status_code))


