from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get('https://www.inmotionhosting.com/shared-hosting')

plans = driver.find_elements(By.XPATH, "//button[@class='imh-term-selector']")

product_list = []
for button in plans:
    driver.execute_script("arguments[0].click();", button)
    time.sleep(5)
    cards = driver.find_elements(By.CLASS_NAME, 'imh-rostrum-card')
    for card in cards:
        name = card.find_element(By.CLASS_NAME, 'imh-rostrum-card-title')
        price = card.find_element(By.CLASS_NAME, 'rostrum-price')
        product_list.append({'name': name.text, 'price': price.text})

for i in product_list:
    print(i)
