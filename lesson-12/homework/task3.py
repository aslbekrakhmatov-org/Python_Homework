from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup
import json
chrome_options = Options()
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--window-position=-1700,-200")
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome()
driver.get("https://www.demoblaze.com/")
time.sleep(3)

laptop_btn = driver.find_element(By.XPATH, "/html/body/div[5]/div/div[1]/div/a[3]")
laptop_btn.click()
time.sleep(3)

next_btn = driver.find_element(By.ID, "next2")
next_btn.click()
time.sleep(5)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "card"))
)

html_content = driver.page_source
soup = BeautifulSoup(html_content, "html.parser")

laptop_data = []

cards = soup.find_all("div", class_ = "card-block")
for card in cards:
    laptop = {}
    laptop["name"] = card.find("h4", class_="card-title").text.strip()
    laptop["price"] = card.find("h5").text.strip()
    laptop["description"] = card.find("p", class_ = "card-text").text.strip()
    laptop_data.append(laptop)

print(laptop_data)
with open("laptops.json", 'w', encoding="utf-8") as file:
    json.dump(laptop_data, file, indent=2)

driver.quit()