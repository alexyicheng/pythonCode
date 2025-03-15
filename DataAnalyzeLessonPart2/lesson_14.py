# 14.03.2025

from DrissionPage._functions.keys import Keys
from DrissionPage._pages.chromium_page import ChromiumPage

page = ChromiumPage()
# 打开网页
url = 'https://www.dangdang.com/'
page.get(url)
page.set.timeouts(2)
# 再搜索框中输入 数据分析
input_tag = page.ele('#key_S')
input_tag.input('数据分析')
# 可以回车，也可以点击放大镜
# input_tag.input(Keys.ENTER)
btn_tag = page.ele('.button')
btn_tag.click()
# 进入到数据页面 获取页面中的数据
# 先获取数据对应整体的标签 li
lis = page.eles('x://ul[@id="component_59"]/li')
count = 1
# print(len(lis))
for li in lis:
    a_tag = li.ele('@name=itemlist-title')
    # 获取标签的属性值
    # 标签.attr(属性名)
    name = a_tag.attr('title')
    # 价格
    span_tag = li.ele('.search_now_price')
    # 获取标签的文本内容
    # 标签.text
    price = span_tag.text
    # 作者
    author_tag = li.ele('@name=itemlist-author')
    # if author_tag == None:
    #     author = '无'
    # else:
    #     author = author_tag.attr('title')
    try: # 尝试检查try中的代码是否有错误
        author = author_tag.attr('title')
    except: # # 处理
        author = '无'
    # 出版日期  span[2]代表获取第二个span标签
    cb_date_tag = li.ele('x:.//p[@class="search_book_author"]/span[2]')
    if cb_date_tag == None:
        cb_date = '无'
    else:
        cb_date = cb_date_tag.text.replace('/','')
    # 出版社
    cbs_tag = li.ele('@name=P_cbs')
    if cbs_tag == None:
        cbs = '无'
    else:
        cbs = cbs_tag.text
    # 评论人数
    comment_num_tag = li.ele('.search_comment_num')
    # 有些书籍是没有评论数
    if comment_num_tag == None:
        # 没有
        comment_num = 0
    else:
        # 有
        comment_num = comment_num_tag.text

    print(count,name,price,author,cb_date,cbs,comment_num)
    count+=1