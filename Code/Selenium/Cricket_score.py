##Internship : Selenium Implementation
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def stats(driver):
    #Opening the Cricket World Cup website
    driver.get("https://www.cricketworldcup.com/")
    #Page loading...
    wait = WebDriverWait(driver, 7)
    #Clicking on the "Stats" link
    standings_link = driver.find_element(By.XPATH, "/html/body/div[3]/div/nav[1]/div/div[3]/ul/li[3]/div[1]")
    standings_link.click()
    driver.implicitly_wait(1) 
    standings_link = driver.find_element(By.XPATH, "/html/body/div[3]/div/nav[1]/div/div[3]/ul/li[3]/div[2]/ul/li[1]")
    standings_link.click()
    # Waiting for the page to load... :)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "wrapper")))
    # Finding the stats using X_PATH and printing it(Most runs, wickets and wins by a team)
    print("Most Runs:")
    first_name = driver.find_element(By.XPATH, "/html/body/div[5]/main/div/div/div[2]/section[1]/div/div[1]/div/div/div[2]/div[2]/a/span/span[1]")
    last_name = driver.find_element(By.XPATH, "/html/body/div[5]/main/div/div/div[2]/section[1]/div/div[1]/div/div/div[2]/div[2]/a/span/span[2]")
    Country = driver.find_element(By.XPATH, "/html/body/div[5]/main/div/div/div[2]/section[1]/div/div[1]/div/div/div[2]/div[2]/div[1]/span")
    Runs = driver.find_element(By.XPATH, "/html/body/div[5]/main/div/div/div[2]/section[1]/div/div[1]/div/div/div[2]/div[2]/div[2]")
    print(first_name.text + " " + last_name.text +" from "+ Country.text +" with "+Runs.text+" runs.")
    print()
    print("Most Wickets: ")
    first_name = driver.find_element(By.XPATH, "/html/body/div[5]/main/div/div/div[2]/section[2]/div/div[2]/div/div/div[2]/div[2]/a/span/span[1]")
    last_name = driver.find_element(By.XPATH, "/html/body/div[5]/main/div/div/div[2]/section[2]/div/div[2]/div/div/div[2]/div[2]/a/span/span[2]")
    Country = driver.find_element(By.XPATH, "/html/body/div[5]/main/div/div/div[2]/section[2]/div/div[2]/div/div/div[2]/div[2]/div[1]/span")
    wickets = driver.find_element(By.XPATH, "/html/body/div[5]/main/div/div/div[2]/section[2]/div/div[2]/div/div/div[2]/div[2]/div[2]")
    print(first_name.text + " " + last_name.text +" from "+ Country.text +" with "+wickets.text+" wickets.")
    print()
    print("Most Wins: ")
    Team_name = driver.find_element(By.XPATH, "/html/body/div[5]/main/div/div/div[2]/section[3]/div/div[2]/div/div/div[2]/div[2]/span/span/span")
    wins = driver.find_element(By.XPATH, "/html/body/div[5]/main/div/div/div[2]/section[3]/div/div[2]/div/div/div[2]/div[2]/div")
    print(Team_name.text + " - "+ wins.text)
    print()

def Standings(driver):
    #Opening the Cricket World Cup website
    driver.get("https://www.cricketworldcup.com/")
    #Page loading...
    wait = WebDriverWait(driver, 7)
    #Clicking on "Standings" link
    standings_link = driver.find_element(By.XPATH, "/html/body/div[3]/div/nav[1]/div/div[3]/ul/li[6]/div")
    standings_link.click()
    #Waiting for that page to load
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "wrapper")))
    driver.implicitly_wait(2)
    #Finding and printing the table data
    table = driver.find_element(By.CLASS_NAME, "table")
    table_head = table.find_element(By.TAG_NAME, "thead")
    table_body = table.find_element(By.TAG_NAME, "tbody")

    #headers
    headers = table_head.find_elements(By.CLASS_NAME, "table-head__cell")
    header_text = [header.text for header in headers]
    header_formatted = "\t".join(header_text)
    print(header_formatted)

    #rows
    rows = table_body.find_elements(By.CLASS_NAME, "table-body")
    i=0
    for row in rows:
        cells = row.find_elements(By.CLASS_NAME, "table-body__cell")
        row_data = [cell.text for cell in cells]
        if(i==1 or i==10):
            row_formatted = "\t ".join(row_data)
        else:
            row_formatted = "\t".join(row_data)
        print(row_formatted)
    print() 

def main():
    #Initiating the driver here in Main...
    driver = webdriver.Firefox()
    print("Browser Automation using Selenium")
    print("---------------------------------")
    print("CWC - 2023")
    print("----------")
    Standings(driver)
    time.sleep(1)
    print("_._._._._._._._")
    print(" Season Stats")
    print("```````````````")
    stats(driver)
    # Closeing the browser
    driver.quit()

if __name__ == '__main__':
    main()