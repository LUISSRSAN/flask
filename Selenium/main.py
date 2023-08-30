from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get()

#price_dollar = driver.find_element(By.CLASS_NAME,value="a-price-whole")
#price_cents = driver.find_element(By.CLASS_NAME,value="a-price-fraction")
#print(f"the price is {price_dollar.text}.{price_cents.text}")


events_times = driver.find_elements(By.CSS_SELECTOR,".event-widget a")
event_names = driver.find_elements(By.CSS_SELECTOR,".event-widget li a")
events = {}

for n in range (len(events_times)-1):
    events[n] = {
        "time":events_times[n].text,
        "name":event_names[n].text,
    }
print(events)




driver.quit()