import requests
from bs4 import BeautifulSoup

string = 'Interview'
new_string = string.replace('e','-',1)
# print(new_string)

url = 'https://www.stepstone.de//jobs--Data-Analyst-Talanx-Group-Reinsurance-Hannover-HDI-AG--11601397-inline.html'
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'referer':'https://www.stepstone.de/work/analyst-data'
}
res = requests.get(url,headers=headers)
soup = BeautifulSoup(res.text,'lxml')
print(soup)
