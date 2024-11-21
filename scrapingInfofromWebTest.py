# 20.11.2024

import requests
from bs4 import BeautifulSoup
import json
import re

url = 'https://de.indeed.com/viewjob?jk=76a69ec2f5c90170&tk=1id5gtl20jtht803&from=hp&vjs=3&advn=8043105035342083&adid=437742118&ad=-6NYlbfkN0AaypzmABWqEvPXCbuGD5b_wYtEVaKRHbyvyKmaYfWRx_bfucMnG2bNRLxMvmA_RN668UaHj3FDTgW9zQTyE32s0Z1q4NveVsvRoXbvlUZpTD82XBiK2_RjDWbqsVtw6oFKaa4jGSrGVyrGzGFeFc-_Nk_DOtk-54ResrEGu9XoXOjawxGaIHdW8FQdLThzHD5SNSXCIC2gJicHKv6ERVghIJiSx2B3Rzd4MSa8-hT-jcc3aat0dTEpJ6qeJFA5mgy-HDPkbRpDNV6J5_uj984X7ZwHdqCEIJHtC3HMD7l3wkqTbQBXvbvNj8OvOmepS1L3XQAxnq0TwV0bHNNNsY4DZYf5XqwaFVYCN7RzMa_jBwh8bdJxG4Zy1glcpPweb0aJ0UxjimPTsrVtqUdTLKY8ltvvgsWMELiPGPM5DMknK3JXk3P_aaXNldckjpfmf2_HZ7AcLs-QTn8q2LcfQckoRXGzm_FtYRgpgbS04cc1Nav5e6AmzRSej0pyPU44ZZg2JXbNz00HNyM7DL2zMzSDPxZ-IzCuf1Pqbm1V8iAmIY8zvpc3DJYqiX6dsEBGI2qDW-xCGhNdE4C0iAtXf3ixqT5hHIMDp2TVXLZFKQ-GOg==&xkcb=SoDB6_M35lp7Z72XZR0CbzkdCdPP&xpse=SoAl6_I35lp5eVRupB0ObzkdCdPP&sjdu=DeHfnKqu11Bqetq9wYuYEujjo88IBFOch9voFao_22DRzOtLdK6dG-JKoCIerWR1nf1314qIVurruWDjQQjUMenr65sXr-gUx2UqUvTNJPmTR4MzyJrz2Bi7FlObqzuXBxIOaKsIFOXdFgMvPJ8bIwo9oN24bLREyezCe-eqk-8H_N_0RYq1gcXIcONoQQUnrjFF45sEW_59-SViwLZ6lg'
# headers = {
#     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
#     'referer':'https://de.indeed.com/?advn=8043105035342083&vjk=76a69ec2f5c90170',
#     'cookie':'CTK=1ib92jqlqioi3800; __cf_bm=64pe.sjqqQzXWL9AoueGX__8mVo447OcyeItvhOTPJQ-1732130840-1.0.1.1-mzYie8_v4.rvfItXaeTxGyV_bKxfaFU9kXsuqjZyfBGWATELfplZuadvtqkPPGkxVDCjllHJyyUFjhJL7jaPqQ; RF="TFTzyBUJoNr6YttPP3kyivpZ6-9J49o-Uk3iY6QNQqKE2fh7FyVgtWvQeAxSOAGH1WK0gAdqZ5c="; LV="LA=1732130840:CV=1732130840:TS=1732130840"; OptanonAlertBoxClosed=2024-11-20T19:27:22.607Z; RQ="q=data+analyst&l=&ts=1732130854124"; LC="co=DE"; cf_clearance=Df640tWpf1FwzoxOcAOgKS9K2oYRDHBQr59.7yn1pkQ-1732130858-1.2.1.1-7vLKxEP_n8o6ROAeEONcObofH1z5_Wj.LVqulJ4jLAPuUIEj9bBuPR8DKmYGPbckCZ76ra9UWIMgD1V7WXC68YEWezb.3MCYygoBqkRIf03x.6Mi6R7IkvxKXaJU9Py5QG_pcH5BbDNYbv2iPkM9Jsv8Jf.yoVmZGQaexpN9cLp8Zb7SsuQbvs2K5OWmLbQzNnq7.a5Q2LXdEbaqNLL57oX7QO4TvNjZUjYm5.RrU7.xZN_XvB9rbWpCh6y7lg0F4PkUQBDXz3aOsjKCcRGh9Du3_l3iu4QZR7zQcAUvy6a56JCTjydnfzGnDUAwfH7e1TAd85tH650XyzJNT3AjaQTZJPW.nLlR4GPd_efm.ZZf4LnvZX4a_uZNKCc62dLP; PPID=""; indeed_rcc="LV:CTK:RQ"; CSRF=L0TNc8OvvXwLCJF15OGVJHASFrOO2yPq; INDEED_CSRF_TOKEN=s1si8qSern2pf0BA7aWpEIp8IL18zdX0; _cfuvid=ovVTlDtHr5.Yn_Nx0zV0qb7IkahLM3XyO70K_V1ajZc-1732131067651-0.0.1.1-604800000; SHARED_INDEED_CSRF_TOKEN=s1si8qSern2pf0BA7aWpEIp8IL18zdX0; RSJC=76a69ec2f5c90170:c55a7505782ac87e:3b6c771abc1175b5:b213d6b37df5f123:70cf12a5c35d858d; OptanonConsent=isGpcEnabled=0&datestamp=Wed+Nov+20+2024+20%3A31%3A24+GMT%2B0100+(Mitteleurop%C3%A4ische+Normalzeit)&version=202409.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=5587c2d7-cae0-49b4-9098-45f5cad922a0&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0%2CC0004%3A0%2CC0007%3A0&intType=2&geolocation=%3B&AwaitingReconsent=false'
# }
# res = requests.get(url,headers=headers)
# soup = BeautifulSoup(res.text,"lxml")

session = requests.Session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
}
res = session.get(url, headers=headers)
print(res.status_code)
print(res.content)  # Nur die ersten 500 Zeichen ausgeben
