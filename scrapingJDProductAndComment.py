# 01.11.2024

# Goal : focus on hot product on JD
# 1.for every comment create file for it
# 2.save comment as txt  picture and video

import requests
import os

# get data from web
headers = {
    'user-agent':'',
    'cookie':''
}
page = 0
while True:
    url = f'{page}'
    res = requests.get(url, headers=headers)

    # filter data
    # json-format
    # json_str = {
    #     'name': 'Daniela',
    #     'age': 32,
    #     'gender': 'woman',
    #     'xxxx': {
    #         'x1': 'xxx',
    #         'x2': 'xxx',
    #         'x3': 'xxx'
    #     }
    # }

    JSON = res.json() # find json data -> change to json-format
    comments = JSON['comments'] # a lot comments dta in json [comments]
    count = 1
    for comment in comments:
        os.makedirs(f'{count}')
        # tracking comments
        print(f'\n===========[{page}page{count}comment]==================')
        text = comment['content'] # comment in [content]
        open(f'{count}/content.txt','w',encoding='utf-8').write(text)

        try:
            # tracking images
            images = comment['images']
            for image in images: # a lot of image data
                imgUrl = 'https:' + image['imgUrl'] # image url is in imgUrl
                # get big pic
                new_imgUrl = imgUrl.replace('n0/s128x96','shaidan/s616x405')
                res1 = requests.get(new_imgUrl)
                open(f'{count}/{imgUrl.split('/')[-1]}','wb').write(res1.content)
        except:
            print('There is no images')

        try:
            # tracking videos
            videos  = comment['videos']
            for video in videos:
                videoUrl = video['remark']
                res2 = requests.get(videoUrl)
                open(f'{count}/{videoUrl.split('?')[0].split('/')[-1]}','wb').write(res2.content)
        except:
            print('There is no video')


        count += 1
    page += 1