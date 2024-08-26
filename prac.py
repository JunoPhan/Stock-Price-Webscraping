import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
import warnings
# Ignore all warnings
warnings.filterwarnings("ignore", category=FutureWarning)

url_netflix ="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html"
url_amazon ="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/amazon_data_webpage.html"

data_amazon = requests.get(url).text
data_netflix = requests.get(url_netflix).text

soup = BeautifulSoup(data_amazon, 'html.parser') 
soup1 = BeautifulSoup(data_netflix,'html.parser')

amazon_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close","Adj Close", "Volume"])
netflix_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close","Adj Close", "Volume"])


for row in soup.find("tbody").find_all("tr"):
    col = row.find_all("td")
    date = col[0].text
    Open = col[1].text
    high = col[2].text
    low =col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text
    amazon_data = pd.concat([amazon_data, pd.DataFrame({"Date":[date], "Open":[Open], "High":[high], "Low":[low], "Close":[close], "Adj Close":[adj_close], "Volume":[volume]})], ignore_index=True)

for row in soup1.find("tbody").find_all("tr"):
    col = row.find_all("td")
    date = col[0].text
    Open = col[1].text
    high = col[2].text
    low =col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text
    netflix_data = pd.concat([netflix_data, pd.DataFrame({"Date":[date], "Open":[Open], "High":[high], "Low":[low], "Close":[close], "Adj Close":[adj_close], "Volume":[volume]})], ignore_index=True)

 #first 5 rows of  stock price dataframe
print("AMAZON STOCK DATAFRAME")
print(amazon_data[0:5])   
print("NETFLIX STOCK DATAFRAME")
print(netflix_data[0:5])

#title attribute
print(soup.title)    
print(soup1.title)

#print(amazon_data.tail(2))  #print last 2 rows of the dataframe

#convert column value to numeric data to plot
amazon_data["Open"] = pd.to_numeric(amazon_data["Open"], errors='coerce')
netflix_data["Open"] = pd.to_numeric(netflix_data["Open"], errors='coerce')

#print(amazon_data.dtypes)
#print(netflix_data.dtypes)

amazon_data.plot(x="Date", y="Open").set_title("Amazon Stock Price Chart")
netflix_data.plot(x="Date", y="Open").set_title("Netflix Stock Price Chart")

plt.legend()
plt.show()
