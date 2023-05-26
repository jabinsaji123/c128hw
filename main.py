from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
from selenium.webdriver.common.by import By
START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
browser = webdriver.Edge("msedgedriver.exe")
browser.get(START_URL)
time.sleep(10)
def scrape():
    headers = ["Brown dwarf","Distance","Mass","Radius"]
    star_data = []
    for i in range(0, 428):
        while True :
         time.sleep(2)  
         soup = BeautifulSoup(browser.text, "html.parser")
         star_table=soup.find_all('table')
         table_rows=star_table[7].find_all('tr')
    for td_tag in soup.find_all("td", attrs={"class", "headerSort"}):
            td_tags = td_tag.find_all("li")
            temp_list = []
            for index, td_tag in enumerate(td_tags):
                if index == 0:
                    temp_list.append(td_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(td_tag.contents[0])
                    except:
                        temp_list.append("")
            star_data.append(temp_list)
    with open("scrapper_3.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(star_data)
scrape()