import os, time, request
import datetime as datetime
import fnmatch #used for matching of names in a string
import subprocess as sp
from selenium import webdriver #driver for the code
from selenium.webdriver.common.keys import Keys # to return keystrokes 
from selenium.webdriver.firefox.options import Options # for options such as headless
from selenium.webdriver.common.by import By #what to except by: ie ID, Class, etc. 
from selenium.webdriver.support.ui import WebDriverWait #used to tell selenium to wait
from selenium.webdriver.support import expected_conditions as EC #used to tell selenium what to wait for an expected condition like an ID appearing or class. 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import WebDriverException
from qbittorrent import Client #used to interact with qb web ui

#Torrent client
qb = Client('http://127.0.0.1:8080')
#Setting browser options
firefox_options = Options()
# firefox_options.add_argument('--headless')

#Driver configuration
driver = webdriver.Firefox(options=firefox_options)
driver.get("https://subsplease.org")

#List of anime to check for
anime = open('/media_share/anime/animewantlist.txt', "r+")

#Used to find the anime in the main list
def findanime():
   try:
      time.sleep(2)
      search = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//*[@id='post-wrapper']/div/div/div[1]/form/input")))
      for a in anime:
         if a == " ":
            continue
         elif a != " ":
            # print(anime)
            # print(a)
            a = a.rstrip()
            # print(a)
            time.sleep(2)
            search.send_keys(a)
            driver.find_element(By.XPATH, "//*[@id='post-wrapper']/div/div/div[1]/form/button").send_keys(Keys.RETURN)
            time.sleep(2)
            search.clear()
            time.sleep(2)
            if EC.text_to_be_present_in_element((By.ID,"releases-table"), a + ".+——"):
               el = driver.find_element(By.ID, "releases-table").text.split("\n")
               # print(el)
               ep_filter(el, a)

            
   finally:
      driver.quit()
      print("Done!")

#Episode list filter, filter used to create list with only episode name text:
def ep_filter(el, a):
   # print(el)
   el = fnmatch.filter(el, (a + "*"))
   # print(el)
   episode_check(el, a)

#Episode checker, to see if episode already downloaded
def episode_check(el, an):
   ani = []
   for e in el:
      with open('/media_share/anime/animelist.txt', "r+") as al:
         for a in al:
            a = ani.append(a.rstrip())
         if e in ani:
            continue
         if e not in ani:
            # print(ani)
            al.write(f'{e}\n')
            magnetgrabber(e, an)

#Used to search for the anime episode and grab the magnet link
def magnetgrabber(e, an):
   search = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//*[@id='post-wrapper']/div/div/div[1]/form/input")))
   search.send_keys(e)
   time.sleep(2)
   driver.find_element(By.XPATH, "//*[@id='post-wrapper']/div/div/div[1]/form/button").send_keys(Keys.RETURN)
   time.sleep(2)
   search.clear()
   href = driver.find_element_by_link_text("1080p")
   magnet = href.get_attribute("href")
   torrent_download(magnet, an)

#Downloads the torrent using qbittorrent
def torrent_download(magnet, an):
   makedir = (f'/media_share/anime/{an}')
   # print(makedir)
   sp.run(['mkdir','-p', makedir])
   qb.download_from_link(magnet, savepath=makedir)

import numpy as np
findanime()




