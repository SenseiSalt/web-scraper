#import libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd


#define variables
url = requests.get('https://www.scrapethissite.com/pages/simple/')
error_msg = 'Failed to Retreive URL'


#Get HTML
if url.status_code == 200:
    html = url.text
else:
    print(error_msg)


#Parse HTML
parser = BeautifulSoup(html, "html.parser")
titles = parser.find_all("h3", class_="country-name")
 
 #Print Country Names
for title in titles:
    print(title.get_text())

#Organize Data
data = {
    "Title": [title.get_text() for title in titles],
}

df = pd.DataFrame(data)
df.to_csv("scraped_data.csv", index=False)
