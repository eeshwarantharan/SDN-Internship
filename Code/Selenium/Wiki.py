import csv
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.wikipedia.org/")

with open('keywords.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        keyword = row["Keyword"]
        search_url = f"https://www.wikipedia.org/wiki/{keyword}"
        driver.execute_script("window.open('', '_blank');")
        driver.switch_to.window(driver.window_handles[-1])
        driver.get(search_url)
        print(f"Opening: {search_url}")