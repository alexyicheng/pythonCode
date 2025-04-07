import requests

num = 0
headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
    }
count = 1
page = 0
while True:
    url = f'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start={num}&limit=20'

    res = requests.get(url,headers=headers,)
    res_data = res.json()

    if len(res_data) == 0:
        break
    for i in res_data:
        title = i['title']
        score = i['score']
        # actors = i['actors'][0]
        actors = ','.join(i['actors'])
        release_Date = i['release_date']
        print(count,title,score,actors,release_Date)
        count += 1
    print(f'current {page+1} page')
    page += 1
    num += 20