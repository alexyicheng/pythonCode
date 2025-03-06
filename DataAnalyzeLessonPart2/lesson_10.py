# 05.03.2025

import requests
pagesite = 0
count = 1
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
}

while True:
    url = f'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start={pagesite}&limit=20'

    res = requests.get(url,headers=headers)
    data = res.json()
    for i in data:
        # option 1
        # if i is None:
        # option 2
        if len(data) == 0:
            break
        # get title
        title = i['title']
        # get release date
        release_date = i['release_date']
        # get score
        score = i['score']
        print(count,title,score,release_date)
        count += 1
    print(f'current {pagesite+1} pagesite')
    pagesite += 1





