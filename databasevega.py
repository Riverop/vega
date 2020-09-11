from pandas import DataFrame
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions
import requests
import time
import random
from selenium import webdriver
import platform
import winsound
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import decimal

if __name__ == "__main__":
    path = ""
    if platform.system() == "Windows":  # checking OS
        path = "./chromedriver.exe"

    email = ("haha@hahast.com")
    password = ("123zxc")
    #chrome_options = Options()
    #chrome_options.add_argument("user-data-dir=selenium")

    driver = webdriver.Chrome(executable_path=path,)
    driver.get("https://ogamex.net/#")
    element = driver.find_element_by_xpath('//*[@id="bodyWrapper"]/footer/div/div[2]/a[2]')
    element.click()
    element = driver.find_element_by_name("Email")
    element.send_keys(email)
    element = driver.find_element_by_name("Password")
    element.send_keys(password)

    element = driver.find_element_by_id("btnLogin")
    element.click()
    time.sleep(4)
    driver.get("https://ogamex.net/connect?serverId=2f965194-a236-41b9-8807-6bcc8e6aa734")

    driver.get("https://vega.ogamex.net/galaxy")
    time.sleep(2)
    moon_data = []
    player = []
    planet_no = []
    galaxy = []
    system = []
    alliance = []
    gal = driver.find_element_by_id("galaxyInput")
    valu = driver.find_element_by_id("systemInput")

    for i in range(1, 6):
        gal.clear()
        gal.send_keys(i)

        for j in range(1, 300):
            valu.send_keys(Keys.BACKSPACE)
            valu.send_keys(Keys.BACKSPACE)
            valu.send_keys(Keys.BACKSPACE)
            time.sleep(float(decimal.Decimal(random.randrange(150, 200)) / 100))
            valu.send_keys(j)
            valu.send_keys(Keys.ENTER)
            time.sleep(float(decimal.Decimal(random.randrange(150, 200)) / 100))
            pagesource = driver.page_source
            soup = BeautifulSoup(pagesource, 'html.parser')
            info = soup.find_all('div', class_="galaxy-col col-player")
            moon = soup.find_all('div', class_="galaxy-col col-moon")
            planet = soup.find_all('div', class_="galaxy-col col-planet-index")
            vega = soup.find_all('div', class_="galaxy-col col-alliance")

            for k in range(15):
                if moon[k].find('div'):
                    moon_data.append("Yes")
                else:
                    moon_data.append("No")
                x = info[k].find('span')
                y = planet[k].find('span')
                z = vega[k].find('span')
                player.append(x.get_text())
                galaxy.append(i)
                system.append(j)
                if z is not None:
                    alliance.append(z.get_text())
                else:
                    alliance.append(" ")
                planet_no.append(y.get_text())

    data = {'Galaxy': galaxy, 'System': system, 'Planet#': planet_no,
            'Moon': moon_data, 'Player': player,'Alliance':alliance,
            }
    df = pd.DataFrame(data)
    filename = datetime.datetime.now().strftime("vega%d%m-%H%M")
    df.to_csv(filename + ".csv")
    #winsound.PlaySound('taunt.wav', winsound.SND_FILENAME)
    driver.close()
