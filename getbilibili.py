# 28.10.2024

import requests

url = 'https://upos-sz-mirroraliov.bilivideo.com/upgcxcode/96/86/500001603038696/500001603038696-1-100022.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1730126124&gen=playurlv2&os=aliovbv&oi=1413094762&trid=79424c123e72420e9506da48d8b49d1fu&mid=0&platform=pc&og=hw&upsig=dd6453d73ee719323d248c0da7a759a0&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform,og&bvc=vod&nettype=0&orderid=0,2&buvid=C0D00AB8-1A3E-1962-A05B-B74FCB285D9858613infoc&build=0&f=u_0_0&agrr=0&bw=13767&logo=80000000'

header = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'referer':'https://www.bilibili.com/video/BV1tAhve2Ecn/?spm_id_from=333.337.search-card.all.click'
}

res = requests.get(url,headers=header)

print(res.content)