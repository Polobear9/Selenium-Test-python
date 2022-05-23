from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

browser = webdriver.Chrome(executable_path=r'C:\Users\User\Desktop\JPyahoo\chromedriver.exe')
browser.get("https://www.yahoo.co.jp/")

WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="Login"]/div/p[1]/a/span')))
login = browser.find_element(By.XPATH, '//*[@id="Login"]/div/p[1]/a/span')
login.click()

WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, 'username')))
login_ID = browser.find_element(By.ID, 'username')
login_ID.send_keys("...") #insert the ID for Yahoo Japan.co.jp

NEXT_Pass = browser.find_element(By.ID, 'btnNext')
NEXT_Pass.click()

WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, 'switchLink')))
LogCheck = browser.find_element(By.ID, 'switchLink')
LogCheck.click()
WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="switchAuthModalContent"]/div/ul/li[2]/a')))
MailLog = browser.find_element(By.XPATH, '//*[@id="switchAuthModalContent"]/div/ul/li[2]/a')
MailLog.click()

browser.set_page_load_timeout(30) #wait for login while insert the code 

WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ToolList"]/ul/li[38]/div/a/p/span[1]/span')))
move_event = browser.find_element(By.XPATH, '//*[@id="ToolList"]/ul/li[38]/div/a/p/span[1]/span')
move_event.click()

WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="cmpbtn"]/div[1]/div[1]/a/img')))
event_select = browser.find_element(By.XPATH, '//*[@id="cmpbtn"]/div[1]/div[1]/a/img')
event_select.click()
WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, 'btnLot')))
first_event = browser.find_element(By.ID, 'btnLot')
first_event.click()

WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="randomBox"]/div/a')))

browser.back()
browser.back()


WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="cmpbtn"]/div[2]/div[1]/a/img')))
second_event = browser.find_element(By.XPATH, '//*[@id="cmpbtn"]/div[2]/div[1]/a/img')
second_event.click()

WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, 'btnLot')))
second_eventjoin = browser.find_element(By.ID, 'btnLot')
second_eventjoin.click()

browser.back()

browser.back()

WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="cmpbtn"]/div[3]/div[1]/a/img')))
last_event = browser.find_element(By.XPATH, '//*[@id="cmpbtn"]/div[3]/div[1]/a/img')
last_event.click()

WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="grouplist"]/label[1]')))
select_join = browser.find_element(By.XPATH, '//*[@id="grouplist"]/label[1]')
select_join.click()

WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, 'btnLot')))
last_eventjoin = browser.find_element(By.ID, 'btnLot')
last_eventjoin.click()

WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="randomBox"]/div/a')))
browser.quit()