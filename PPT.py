# 18.10.2024
import re
import requests

page = 1

while True:
    if page == 1:
        url2 = 'https://www.ypppt.com/moban/'
    else:
        url2 = f'https://www.ypppt.com/moban/list-{page}.html'
    res2 = requests.get(url2)
    if res2.status_code == 404: # from page 1 ... to one Time reach 404
        break
    res2.encoding ='utf-8'
    # print(res2.text)
    fileid = re.findall('<a href="/article/.*?/(.*?).html"class="img_preview"',res2.text)
    # print(fileid)

    for id in fileid:
        # search download url
        url1 = 'https://www.ypppt.com/p/d.php?aid='+id
        res1 = requests.get(url1)
        # print(res1.text)
        url = re.findall('<li><a href="(.*?)">下载地址1</a></li>', res1.text)[0]
        # print(url)
        if '.html' in url or 'pan.baidu' in url:
        # if this file is html or storage by baidu cloud
            continue
        filename = re.findall('<title>(.*?) - 下载页</title>', res1.text)[0]
        filetype = url.split(".")[-1]

        # request download website
        print(f'downloading{filename}.{filetype} website={url}')
        res = requests.get(url)
        open(f'PPT/{filename}.{filetype}', 'wb').write(res.content)
    page += 1


