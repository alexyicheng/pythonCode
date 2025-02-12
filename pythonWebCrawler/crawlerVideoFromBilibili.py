# 09.02.2025

import requests
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.io.VideoFileClip import VideoFileClip

url ="https://upos-sz-estgoss.bilivideo.com/upgcxcode/67/10/27833861067/27833861067-1-100050.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1739274756&gen=playurlv2&os=upos&oi=2936782416&trid=1e0b4e1b3ef34ecaa26a9e0594aaa920u&mid=433316204&platform=pc&og=cos&upsig=1b844fa8411fdf58ecb336fb028e4d86&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform,og&bvc=vod&nettype=0&orderid=0,3&buvid=58E588D4-C7D6-EE4A-FC88-B329BE7B941337981infoc&build=0&f=u_0_0&agrr=1&bw=78361&logo=80000000"

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.3',
    'referer':'https://www.bilibili.com/video/BV1uzcVemENG/?spm_id_from=333.788.player.player_end_recommend_autoplay&vd_source=3c30c2c0feb825482a825818adba3bce'
}
res = requests.get(url,headers=headers)
open('NiDeYuMengYa.mp4','wb').write(res.content)

url_1 ="https://upos-sz-estgoss.bilivideo.com/upgcxcode/67/10/27833861067/27833861067-1-30280.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1739274756&gen=playurlv2&os=upos&oi=2936782416&trid=1e0b4e1b3ef34ecaa26a9e0594aaa920u&mid=433316204&platform=pc&og=cos&upsig=46264e6c05d1e81bb1983af247933b24&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform,og&bvc=vod&nettype=0&orderid=0,3&buvid=58E588D4-C7D6-EE4A-FC88-B329BE7B941337981infoc&build=0&f=u_0_0&agrr=1&bw=13882&logo=80000000"

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.3',
    'referer':'https://www.bilibili.com/video/BV1uzcVemENG/?spm_id_from=333.788.player.player_end_recommend_autoplay&vd_source=3c30c2c0feb825482a825818adba3bce'
}
res1 = requests.get(url_1,headers=headers)
open('NiDeYuMengYa.mp3','wb').write(res1.content)
#
video = VideoFileClip('NiDeYuMengYa.mp4')
audio = AudioFileClip('NiDeYuMengYa.mp3')
final = video.with_audio(audio)
final.write_videofile('fullVidoe.mp4')