# 15.03.2025

from DrissionPage import ChromiumPage
import openpyxl

page = ChromiumPage()
url = 'https://www.mi.com/shop/category/list'
page.get(url)

divs = page.eles('.category-box')
# print(len(divs))

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = 'category'
sheet.append(['ProductName'])


for div in divs:
    title = div.ele('.title').text.replace('','')
    # title = page.ele('x:./h2[@class="title"]')
    print(title)
    sheet.append([title])
    list_1 = div.eles('x:./ul[@class="category-list"]/li')
    for e in list_1:
        name = e.ele('.name').text
        print(name)
        sheet.append([name])

wb.save('XiaoMiCategory.xlsx')