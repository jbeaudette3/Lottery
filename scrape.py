import math
import pandas as pd
import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def get_day_data(i):
    day = {}
    
    dates = driver.find_elements(By.CLASS_NAME, 'dbg-results__dates-info')
    day['Date'] = dates[i].text
    
    n1 = f'result-line-primary-0-{i+1}'
    num1 = driver.find_elements(By.ID, n1)[0].text.strip()
    day['Num1'] = num1
    
    n2 = f'result-line-primary-1-{i+1}'
    num2 = driver.find_elements(By.ID, n2)[0].text.strip()
    day['Num2'] = num2
        
    n3 = f'result-line-primary-2-{i+1}'
    num3 = driver.find_elements(By.ID, n3)[0].text.strip()
    day['Num3'] = num3
        
    n4 = f'result-line-primary-3-{i+1}'
    num4 = driver.find_elements(By.ID, n4)[0].text.strip()
    day['Num4'] = num4
        
    n5 = f'result-line-primary-4-{i+1}'
    num5 = driver.find_elements(By.ID, n5)[0].text.strip()
    day['Num5'] = num5
    
    p = f'result-line-secondary-0-{i+1}'
    pb = driver.find_elements(By.ID, p)[0].text.strip()
    day['Power'] = pb
    
    return day


site = 'https://www.illinoislottery.com/dbg/results/megamillions?page='
data_list = []
driver = webdriver.Safari()

i = '1'
full_site = site + str(i)
driver.get(full_site)
print(i)
time.sleep(5)

for i in range(10):
    data_list.append(get_day_data(i))

total_page_count = driver.find_element(By.CLASS_NAME, 'pagination-controls').text.split()[-1]
pages = math.ceil(int(total_page_count)/10)

for page in range(2, pages):
    print(page)
    full_site = site + str(page)
    driver.get(full_site)
    time.sleep(5)
    for i in range(10):
        data_list.append(get_day_data(i))

driver.quit()
df = pd.DataFrame(data_list)

# clean up on dataframe
df[['DOW', 'Month', 'Day', 'Year']] = df['Date'].str.split(expand = True)
df['Day'] = df['Day'].str.replace(',', '')
df = df[['Date', 'DOW', 'Month', 'Day', 'Year'\
        'Num1', 'Num2', 'Num3', 'Num4', 'Num5', 'Power']]

# save
df.to_csv('lotto.csv', index = False)
