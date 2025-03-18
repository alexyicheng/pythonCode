# https://www.mi.com/shop/search?keyword=%E6%89%8B%E6%9C%BA

from DrissionPage import ChromiumPage

page = ChromiumPage()

page.get('https://www.mi.com/shop/search?keyword=%E6%89%8B%E6%9C%BA')

# print(page.ele('x://div[@class="price-info"]/span'))

# get the content of page
divs = page.eles('.goods-item')
count = 1
for div in divs:
    print(f'============{count}==============')
    # get the url
    d_url = div.ele('x:./a').attr('href')
    # open new tab
    d_page = page.new_tab(d_url)
    # get the version of handy, smartphone and so on
    version_box = d_page.ele('x://div[@class="buy-option"]/div[1]')
    if version_box == None:
        continue
    version_list = version_box.eles('tag:li')
    for e in version_list:
        # get the version of it
        version_name = e.attr('title')
        print(version_name)
        e.click()
        color_box = d_page.ele('x://div[@class="buy-option"]/div[2]')
        color_list = color_box.eles('tag:li')
        # get current color
        for color in color_list:
             color_name = color.attr('title')
             print(color_name)
        batch_box = d_page.eles('x://div[@class="batch-box"]/ul/li/a',timeout=1)
        if len(batch_box) == 0:
            price_tag = d_page.ele('x://div[@class="price-info"]/span')
            print(price_tag.text)
        # get current batch
        for batch in batch_box:
            batch.click()
            price_tag = d_page.ele('x://div[@class="price-info"]/span')
            print(batch.text,price_tag.text)
        print('_______________________')

    d_page.close()
    count += 1