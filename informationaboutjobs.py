# 28.10.2024

# use scraping of python to catch information from StepStone to know
# which information is necessary of this job

import requests
from bs4 import BeautifulSoup
import json
import re

job_title = input('Geben Sie bitte den Job, der Sie mehr wissen wollen :) :')
pages = int(input('Geben Sie bitte an, wie viel Seite an Informationen benötigen Sie für die Visualisierung:'))
# job_title = 'Data Analyst'

required_skills = []
skill_words = []


url = f'https://www.stepstone.de/work/{job_title}'
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
}
res = requests.get(url,headers=headers)
soup = BeautifulSoup(res.text,"lxml")

for i in range(0,pages):
    # for the case if only 1 page is required
    if i <= 1:
        print('Its start') # for testing
        url = f'https://www.stepstone.de/work/{job_title}'
        links = []
        for link in soup.find_all('a', {'class': ['res-1foik6i']}):
            links.append('https://www.stepstone.de/' + link.get("href"))
        print(links)

        # open the link
        for new_url in links:
            print('i am running')
            rounds = 0  # count how many links was opened
            header = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
                'referer': url
            }
            print(new_url)
            print(rounds)
            rounds = + 1

            # # get the information of the link
            res2 = requests.get(new_url, headers=header)
            # web_content = res2.text
            soup2 = BeautifulSoup(res2.text, 'lxml')
            # print(soup2)

            # extract the qualifications from <script type="application/ld+json">*</script>
            extract_qualification = [json.loads(x.string) for x in soup2.find_all('script', type='application/ld+json')]
            print(extract_qualification)
            try:
                # extract the skills of job
                for skill in extract_qualification:
                    skill_info = skill['description']
                    # print(skill_info)
                    # print(type(skill_info))
                    infos = BeautifulSoup(skill_info, 'lxml')
                    # filter_infos_position = infos.find_all('h4')
                    # print(filter_infos_position)
                    # [<h4>Ihre Aufgaben</h4>, <h4>Ihr Profil</h4>, <h4>Unser Angebot</h4>, <h4>Contact</h4>]
                    filter_infos = infos.find_all('ul')[1]
                    skill_for_your_job = filter_infos.find_all('li')
                    # print(skill_for_your_job)

                    for skills in skill_for_your_job:
                        required_skills.append(str(skills))
                    # print(required_skills)
                    # extract the skill of job to key word

                    for r_s in required_skills:
                        skill_row = re.findall('<li>(.+)</li>', r_s)
                        for word in skill_row:
                            skill_words.extend(word.split())
                    open(f'{job_title}_Infomations.txt','w',encoding='utf-8').write(skill_words)
                    # print(skill_words)
            except(requests.RequestException, Exception):
                print('something goes wrong :',new_url)
                continue
    else:
        # case for more than 1 page is required
        print(f'{i}.page started,just to sure that works, too')
        url = f'https://www.stepstone.de/work/{job_title}?page={pages}'
        # Get all links of the jobs
        links = []
        for link in soup.find_all('a',{'class':['res-1foik6i']}):
            links.append('https://www.stepstone.de/'+link.get("href"))
        # print(links)

        for new_url in links:
            print('i am running')
            rounds = 0  # count how many links was opened
            header = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
                'referer': url
            }
            print(new_url)
            print(rounds)
            rounds = + 1

            # # get the information of the link
            res2 = requests.get(new_url, headers=header)
            # web_content = res2.text
            soup2 = BeautifulSoup(res2.text, 'lxml')
            # print(soup2)

            # extract the qualifications from <script type="application/ld+json">*</script>
            extract_qualification = [json.loads(x.string) for x in soup2.find_all('script', type='application/ld+json')]
            print(extract_qualification)
            try:
                # extract the skills of job
                for skill in extract_qualification:
                    skill_info = skill['description']
                    # print(skill_info)
                    # print(type(skill_info))
                    infos = BeautifulSoup(skill_info, 'lxml')
                    # filter_infos_position = infos.find_all('h4')
                    # print(filter_infos_position)
                    # [<h4>Ihre Aufgaben</h4>, <h4>Ihr Profil</h4>, <h4>Unser Angebot</h4>, <h4>Contact</h4>]
                    filter_infos = infos.find_all('ul')[1]
                    skill_for_your_job = filter_infos.find_all('li')
                    # print(skill_for_your_job)

                    for skills in skill_for_your_job:
                        required_skills.append(str(skills))
                    # print(required_skills)
                    # extract the skill of job to key word

                    for r_s in required_skills:
                        skill_row = re.findall('<li>(.+)</li>', r_s)
                        for word in skill_row:
                            skill_words.extend(word.split())
                print(skill_words)
            except(requests.RequestException, Exception):
                print('something goes wrong :', new_url)
                continue







# for i in range(1,pages):
#     if i == 1:
#         url = f'https://www.stepstone.de/work/{job_title}'
#     else:
#         url = f'https://www.stepstone.de/work/{job_title}?page={pages}'





