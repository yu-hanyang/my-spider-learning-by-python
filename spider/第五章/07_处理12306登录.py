from selenium.webdriver import Chrome
from chaojiying import Chaojiying_Client
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.chrome.options import Options
chaojiying = Chaojiying_Client('17369627926', 'younger12138', '96001')	#用户中心>>软件ID 生成一个替换 96001
												#本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
option =Options()
option.add_argument('--disable-blink-features=AutomationControlled')

web=Chrome(options=option)
web.get('https://kyfw.12306.cn/otn/resources/login.html')

time.sleep(3)
web.find_element_by_xpath('/html/body/div[2]/div[2]/ul/li[2]/a').click()
time.sleep(3)

verify_img_element = web.find_element_by_xpath('//*[@id="J-loginImg"]')
dic=chaojiying.PostPic(verify_img_element.screenshot_as_png, 9004)
result=dic['pic_str']
rs_list = result.split('|')
for rs in rs_list:
    x,y=map(int,rs.split(','))
    ActionChains(web).move_to_element_with_offset(verify_img_element,x,y).click().perform()
time.sleep(1)
web.find_element_by_xpath('//*[@id="J-userName"]').send_keys('')#用户名
web.find_element_by_xpath('//*[@id="J-password"]').send_keys('')#密码



#点击登录
web.find_element_by_xpath('//*[@id="J-login"]').click()
time.sleep(5)

btn = web.find_element_by_xpath('//*[@id="nc_1_n1z"]')

ActionChains(web).drag_and_drop_by_offset(btn,300,0).perform()
