
import re
import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

GOOGLE_FORM_LINK = 'https://docs.google.com/forms/d/e/1FAIpQLScnAHPNrOdv_V-UvSwtaCEVLjSlXzzJMI54hWnbIOwKipaW6g/viewform'
WEB_SITE_URL = 'https://appbrewery.github.io/Zillow-Clone/'

response = requests.get(url=WEB_SITE_URL)
soup = BeautifulSoup(response.text, "html.parser")

addresses = []
prices = []
links = []

def clean_address(address):
    address = re.sub(r"[\n|]", " ", address)
    address = re.sub(r"\s+", " ", address)
    return address.strip()

listings = soup.find_all("div", class_="StyledPropertyCardDataWrapper")
for listing in listings:
    address = listing.find("address").get_text() if listing.find("address") else "N/A"
    cleaned_address = clean_address(address)
    addresses.append(cleaned_address)
    
    price = listing.find(class_="PropertyCardWrapper__StyledPriceLine").get_text() if listing.find(class_="PropertyCardWrapper__StyledPriceLine") else "N/A"
    clean_price = re.sub(r"[^\d$,]", "", price)
    prices.append(clean_price)
    links.append(listing.find("a")["href"] if listing.find("a") else "N/A")

driver = webdriver.Chrome(options=chrome_options)
for n in range(len(addresses)):
    driver.get("https://docs.google.com/forms/d/1w5zn8GhjDd_DzN001i3B8edPvyOAACVe4lFi7ZFBzII/edit")
    time.sleep(2)

    input_fields = driver.find_elements(By.CSS_SELECTOR, 'input.whsOnd.zHQkBf')

    if len(input_fields) >= 3:
        input_fields[0].send_keys(addresses[n])
        input_fields[1].send_keys(prices[n])
        input_fields[2].send_keys(links[n])
    
    submit_button = driver.find_element(By.CSS_SELECTOR, 'div.uArJ5e.UQuaGc.Y5sE8d.VkkpIf')
    submit_button.click()
    time.sleep(2)

print(f"Successfully submitted {len(addresses)} listings to the form.")