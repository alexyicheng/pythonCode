# 28.10.2024

# use scraping of python to catch information from StepStone to know
# which information is necessary of this job

import requests
from bs4 import BeautifulSoup
import json
import re

# job_title = input('Geben Sie bitte den Job, der Sie mehr wissen wollen :) :')
# pages = int(input('Geben Sie bitte an, wie viel Seite an Informationen benötigen Sie für die Visualisierung:'))
job_title = 'Data Analyst'
url = f'https://www.stepstone.de/work/{job_title}'
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
}
res = requests.get(url,headers=headers)
soup = BeautifulSoup(res.text,"lxml")


# Get all links of the jobs
links = []
for link in soup.find_all('a',{'class':['res-1foik6i']}):
    links.append('https://www.stepstone.de/'+link.get("href"))
# print(links)

# open the link
new_url = links[3]
header ={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'referer':url
}
# print(new_url)

# # get the information of the link
res2 = requests.get(new_url,headers=header)
# web_content = res2.text
soup2 = BeautifulSoup(res2.text,'lxml')

# extract the qualifications from <script type="application/ld+json">*</script>
extract_qualification = [ json.loads(x.string) for x in soup2.find_all('script', type='application/ld+json') ]
# print(extract_qualification)

# extract the skills of job
for skill in extract_qualification:
    skill_info = skill['description']
    print(skill_info)
    print(type(skill_info))
    # for qualify in skill_info['Diesen fachlichen Background bringst Du mit']:
    #     print(qualify)
    # skills = re.findall('<h4>Diesen fachlichen Background bringst Du mit:</h4><p></p><ul>(.*?)</ul>',skill_info)
    # print(skills)
#



# for i in range(1,pages):
#     if i == 1:
#         url = f'https://www.stepstone.de/work/{job_title}'
#     else:
#         url = f'https://www.stepstone.de/work/{job_title}?page={pages}'

