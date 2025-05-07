from DrissionPage._pages.chromium_page import ChromiumPage

page = ChromiumPage()
url = 'https://www.google.de/?hl=de'
page.get(url)

input_tag = page.ele('#APjFqb')
input_tag.input('python\n')  # \n simuliert die Enter-Taste
