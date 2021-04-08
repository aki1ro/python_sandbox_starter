import os
import time
import requests
import json
import pprint
import datetime as datetime
from browsermobproxy import Server
# from seleniumwire import webdriver as webdriver_capture
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
   # driver.quit() quits driver

#Searches for Anime and clicks it, then finds the episodes asked for (episode 1 as test for now) 
try:
   link = driver.find_element_by_link_text("Boku no Hero Academia Season 5")
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
         # driver.switch_to.frame(driver.find_element_by_xpath('/html/body/div/button'))
         # frame.click()
         print("Yay!!")

finally:
   print("Starting .ts capture")
   
# pprint.pprint(proxy.har)


fetched = []
while checkdriver() == True:
   for ent in proxy.har['log']['entries']:
      _url = ent['request']['url']
      _response = ent['response']
      
    #make sure havent already downloaded this piece
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

print("Done with Capture code")
#Function to filter the objects using JSON(Javascript Object Notation) aka data interchange objects and generates a log entry for each request found.
# def process_browser_log_entry(entry):
#     response = json.loads(entry['message'])['message']
#     return response

# while checkdriver() == True:
#    with open ("Testlog.txt", 'wt') as f:
#       log = driver.get_log('performance')
#       events = [process_browser_log_entry(entry) for entry in log]
#       events = [event for event in events if 'Network.response' in event['method']]
#    for e in events:
#       url = e['params']['url'].endswith('ts')
#       r1 = requests.get(url, stream=True)
#       if(r1.status_code == 200):
#          with open('Test_Video.mpeg', "ab") as f:
#             for chunk in r1.iter_content(chunk_size=1024):
#                f.write(chunk)
#       else:
#          print("Received unexpected status code {}".format(r1.status_code))
# while checkdriver() == True:
#    log = driver.get_log('performance')
#    events = [process_browser_log_entry(entry) for entry in log]
#    events = [event for event in events if 'Network.responseReceived' in event['method']]
#    for e in events:
#       if e['params']['response']['url'].endswith('.ts'):
#           url = e['params']['response']['url']
#           r1 = requests.get(url, stream=True)
#           if(r1.status_code == 200):
#             with open('Test_Video.mpeg', "ab") as f:
#                for chunk in r1.iter_content(chunk_size=1024):
#                   f.write(chunk)
#           else:
#              print("Received unexpected status code {}".format(r1.status_code))
      








# def process_log(entry):
#       response = json.loads(entry["message"])["message"]
#       return response  
   
# log = driver.get_log('performance')
# events = [process_log(entry) for entry in log]
# events = [event for event in events if 'Network.responseReceived' in event ['method']]
# with open ("Log.text", "w") as out:
#    for event in events:
#       pprint.pprint(event, stream=out)

# while checkdriver() == True:
   # browser_log = log
   # events = [process_log(log) for entry in browser_log]
   # events = [event for event in events if 'Network.response' in event ['method']]
   
   
# print(events)
#Starts the network capture by creating logs


# take the log items found and put them into a text file 

# l.write('%s\n' % event) #The %s token allows me to insert (and potentially format) a string. Notice that the %s token is replaced by whatever I pass to the string after the % symbol




# with open ("Log.txt, 'wt'") as o:
#    for event in events:
#       o.write(event)
#       # pprint.pprint(event, stream=out)





# def process_log(entry):
#    response = json.loads(entry['message'])['message']
#    return response

# while True:
#    driver = driver.get(driver)
#    browser_log = driver.get_log('performance')
#    events = [process_log(entry) for entry in browser_log]
#    events = [event for event in events if 'Network.response' in event['method']]



# for x in anime:
#    for i in element:
#       if i == x:
#          link = driver.find_elements_by_link_text(x)
#          for e in episodes:
#             if e > myepisode
#             then download e


#          driver.back()
#          driver.back()

# driver.back() #used to go back a page
# driver.back()
# driver.forward() #used to go forward a page
# search.send_keys("Hero Acadamia")
# search.send_keys(Keys.RETURN)

# driver.quit()



