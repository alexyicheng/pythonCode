# 18.03.2025

from openpyxl import Workbook
from DrissionPage import ChromiumPage

page = ChromiumPage()
url = 'https://www.cwl.gov.cn/ygkj/wqkjgg/'
page.get(url)

# get all data of table <tr data-alias="undefined" >
trs = page.eles('@data-alias=undefined')
# print(len(trs))

wb = Workbook()
# sheet = wb.active
# sheet.title = 'lotterie'
# sheet.append(['ID','OpenDate','WinCode','firstPrice','secondPrice','sales','pool','date'])
pagenumber = 1
while True:
    sheet = wb.create_sheet(f'{pagenumber}.page')
    sheet.append(['ID','OpenDate','WinCode','firstPrice','secondPrice','sales','pool','date'])

    trs = page.eles('@data-alias=undefined')
# get the single data of row
    for tr in trs:
        tds = tr.eles('tag:td')
        data = []
        # tds = tr.eles('x://tr//td')
        for td in tds[:-1]:
            data.append(td.text)
        sheet.append(data)
    next_tag = page.ele('.layui-laypage-next')
    if 'layui-disabled' in next_tag.attr('class'):
        break
    next_tag.click()
    pagenumber += 1

wb.remove(wb.active)
wb.save('LotterieNumber.xlsx')