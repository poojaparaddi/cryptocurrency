import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
def get_crypto_data(coin):
    url = f"https://coinmarketcap.com/{coin}/"
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(service=Service('/path/to/chromedriver'), options=options)
    driver.get(url)
    
    data = {
        "price": driver.find_element(By.XPATH, '...').text,
        "price_change": driver.find_element(By.XPATH, '...').text,
        "market_cap": driver.find_element(By.XPATH, '...').text,
        "market_cap_rank": driver.find_element(By.XPATH, '...').text,
        "volume": driver.find_element(By.XPATH, '...').text,
        "volume_rank": driver.find_element(By.XPATH, '...').text,
        "volume_change": driver.find_element(By.XPATH, '...').text,
        "circulating_supply": driver.find_element(By.XPATH, '...').text,
        "total_supply": driver.find_element(By.XPATH, '...').text,
        "diluted_market_cap": driver.find_element(By.XPATH, '...').text,
        "contracts": [...],
        "official_links": [...],
        "socials": [...]
    }
    driver.quit()
    return data