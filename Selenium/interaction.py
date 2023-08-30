from selenium import webdriver


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver_path = "/Users/luis-santiago/Downloads/chromedriver"

# Your code goes here


driver = webdriver.Chrome(driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
article_count = driver.find_element_by_css_selector("#articlecount a")
print(article_count.text)