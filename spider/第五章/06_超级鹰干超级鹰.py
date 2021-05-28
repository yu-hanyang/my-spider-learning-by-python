from selenium.webdriver import Chrome
from chaojiying import Chaojiying_Client
import time
web = Chrome()

web.get('http://www.chaojiying.com/user/login/')

img = web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/div/img').screenshot_as_png

chaojiying = Chaojiying_Client('17369627926', 'younger12138', '96001')	#用户中心>>软件ID 生成一个替换 96001
												#本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
dic=chaojiying.PostPic(img, 1902)

verfiy_code = dic['pic_str']

web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[1]/input').send_keys('17369627926')
web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[2]/input').send_keys('younger12138')
web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[3]/input').send_keys(verfiy_code)
time.sleep(5)
web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[4]/input').click()