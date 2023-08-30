import requests
import lxml
from bs4 import BeautifulSoup

URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

response = requests.get(URL)
header = {


response . requests.get(URL,headers=header)
soup = BeautifulSoup(response.content,"lxml")
print(soup.prettify())
