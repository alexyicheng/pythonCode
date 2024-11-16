# 15.11.2024

# panic buy url of JD: https://item.jd.com/100008000371.html

from DrissionPage import ChromiumPage
from datetime import datetime
import time

# Panic buying / Snap up
url = input('please insert the panic buying URL:')
time_sj = input('please insert your time(YYYY-MM-DD HH:MM:SS)')
# change the string to datetime format (YYYY-MM-DD HH:MM:SS)
puer_time = datetime.strptime(time_sj,'%Y-%m-%d %H:%M:%S')
while datetime.now() < puer_time:
    time.sleep(1)

# start Browser
driver = ChromiumPage() # FirefoxPage()

# open the panic buying url
driver.get(url)

# add item into shopping basket #menas id .for class  click() click mouse
driver.ele('css:#InitCartUrl').click()

# go to pay shopping basket
driver.ele('css:#GotoShoppingCart').click()

# pay shopping basket
driver.ele('css:.common-submit-btn').click()

driver.ele('css:.checkout-submit').click()

print('succeeded')