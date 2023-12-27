from bs4 import BeautifulSoup
import requests

url = 'https://www.amazon.com/dp/0399588612/ref=s9_acsd_al_bw_c2_x_1_i?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-14&pf_rd_r=P5J2JVXGBCQKRVV2CE26&pf_rd_t=101&pf_rd_p=5999b405-7142-44f8-ae3f-b70645ed1201&pf_rd_i=283155'
custom_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36', 'accept-language': 'en-US,en;q=0.9'}

response = requests.get(url, headers=custom_headers)
soup = BeautifulSoup(response.text, "lxml")

image_element = soup.select_one('#landingImage')
image = image_element.attrs.get('src')

print(image)