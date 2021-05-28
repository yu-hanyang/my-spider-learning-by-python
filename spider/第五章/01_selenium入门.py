from selenium.webdriver import Chrome

web = Chrome()

web.get('https://www.baidu.com')
print(web.title)