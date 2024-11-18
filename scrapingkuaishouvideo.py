#07.11.2024

import requests

url = 'https://www.kuaishou.com/graphql'

cursor = '' #empty
count = 1

while True:

    data = {
    'operationName':"visionProfilePhotoList",
    'query':"fragment photoContent on PhotoEntity {\n  __typename\n  id\n  duration\n  caption\n  originCaption\n  likeCount\n  viewCount\n  commentCount\n  realLikeCount\n  coverUrl\n  photoUrl\n  photoH265Url\n  manifest\n  manifestH265\n  videoResource\n  coverUrls {\n    url\n    __typename\n  }\n  timestamp\n  expTag\n  animatedCoverUrl\n  distance\n  videoRatio\n  liked\n  stereoType\n  profileUserTopPhoto\n  musicBlocked\n  riskTagContent\n  riskTagUrl\n}\n\nfragment recoPhotoFragment on recoPhotoEntity {\n  __typename\n  id\n  duration\n  caption\n  originCaption\n  likeCount\n  viewCount\n  commentCount\n  realLikeCount\n  coverUrl\n  photoUrl\n  photoH265Url\n  manifest\n  manifestH265\n  videoResource\n  coverUrls {\n    url\n    __typename\n  }\n  timestamp\n  expTag\n  animatedCoverUrl\n  distance\n  videoRatio\n  liked\n  stereoType\n  profileUserTopPhoto\n  musicBlocked\n  riskTagContent\n  riskTagUrl\n}\n\nfragment feedContentWithLiveInfo on Feed {\n  type\n  author {\n    id\n    name\n    headerUrl\n    following\n    livingInfo\n    headerUrls {\n      url\n      __typename\n    }\n    __typename\n  }\n  photo {\n    ...photoContent\n    ...recoPhotoFragment\n    __typename\n  }\n  canAddComment\n  llsid\n  status\n  currentPcursor\n  tags {\n    type\n    name\n    __typename\n  }\n  __typename\n}\n\nquery visionProfilePhotoList($pcursor: String, $userId: String, $page: String, $webPageArea: String) {\n  visionProfilePhotoList(pcursor: $pcursor, userId: $userId, page: $page, webPageArea: $webPageArea) {\n    result\n    llsid\n    webPageArea\n    feeds {\n      ...feedContentWithLiveInfo\n      __typename\n    }\n    hostName\n    pcursor\n    __typename\n  }\n}\n",
    'variables':{'userId': "3xarxa8qvybzjpe", 'pcursor': cursor, 'page': "profile"}
    }
    # fake info
    wz = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        'cookie':'kpf=PC_WEB; clientid=3; did=web_5080091810e4d0bbe41656e4d60a521c; kpn=KUAISHOU_VISION',
        'referer':'https://www.kuaishou.com/profile/3xarxa8qvybzjpe'
    }

    res = requests.post(url,json=data,headers=wz)

    # print(res.text)
    JSON = res.json() # transform to json

    # pcursor = JSON['data']['visionProfilePhotoList']['pcursor']

    # Get video url
    try:
        videos = JSON['data']['visionProfilePhotoList']['feeds']
    # for the case if the kuaishou server doesnot give you the videoUrl
    except:
        break
    # get the url of videos 1 by 1
    for video in videos:
        videoUrl = video['photo']['photoH265Url']
        # download the video as mp4 in your KuaishouSM File
        try:
            print(count,videoUrl)
            res2 = requests.get(videoUrl)
            open(f'KuaiShouSM/{count}_sexymilf.mp4', 'wb').write(res2.content)
            count += 1
        # fot the case if the something goes wrong skip it - Donot stop the programm
        except (requests.RequestException, Exception):
            continue
    cursor = JSON['data']['visionProfilePhotoList']['pcursor']

    # turn the page on website
    # 1) page pn
    # 2) cursor pcursor xcursor mcursor tcursor