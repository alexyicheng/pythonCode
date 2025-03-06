# 04.03.2025

import requests

url = ('https://v3-dy-o.zjcdn.com/fe1b9a2169f929b9ed73396966033761/67c71a4e/video/tos/cn/tos-cn-ve-15/o8Pt1ixEAQAoiX91yMP7YZIMOxOyIxmTKBFgc/?a=6383&ch=10010&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=464&bt=464&cs=0&ds=6&ft=bvTKJiQ6pUZ-fumrejO1ikl9aApXJsYZvrK3_jSqto0g3cI&mime_type=video_mp4&qs=12&rc=ZWQ2PDNpNjw1NWg1ZGQ8O0BpM2ZubWs5cnc2djMzNGkzM0AvYGBhNWBgNV8xYl8wNDQzYSNtaGRuMmQ0MGhgLS1kLWFzcw%3D%3D&btag=80000e00010000&dy_q=1741090830&feature_id=46a7bb47b4fd1280f3d3825bf2b29388&l=20250304202029B9FD1E89D150C316755E&__vid=7433246665311571200')

res = requests.get(url)

with open('jujingyi.mp4','wb') as f:
    f.write(res.content)