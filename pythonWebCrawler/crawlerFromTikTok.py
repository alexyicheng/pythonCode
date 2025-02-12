# 09.02.2025

import requests

URL = 'https://v3-dy-o.zjcdn.com/5e3ab3913594998e56c06ddacd772208/67a8e6b2/video/tos/cn/tos-cn-ve-15/o8ZEAXvhPK92I6CICFPgod4QBiuASiQBOzQEK/?a=6383&ch=10010&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=928&bt=928&cs=0&ds=6&ft=bvTKJiQ6pUZ-fumrejO1ikl9aApC5gjZvrKi11S-to0g3cI&mime_type=video_mp4&qs=12&rc=ODVmM2RoNDs3N2dpPGVnM0Bpaml2NW05cnc5eDMzNGkzM0AzNmJiMzA2Xi0xMi41Y18yYSMtaWZvMmQ0cWhgLS1kLS9zcw%3D%3D&btag=c0000e00010000&cc=1f&cquery=100B_100x_100z_100o_101n&dy_q=1739111536&feature_id=46a7bb47b4fd1280f3d3825bf2b29388&l=2025020922321521729991BF62E3B66007&req_cdn_type=&__vid=746934278989821'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    'Referer':'https://www.douyin.com/'
}

res = requests.get(URL,headers=headers)

print(res.status_code)

open('firstTiktokVideo.mp4','wb').write(res.content)
