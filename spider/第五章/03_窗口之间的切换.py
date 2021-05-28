from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time

web =Chrome()
# web.get('http://lagou.com')
# web.find_element_by_xpath('//*[@id="changeCityBox"]/p[1]/a').click()
#
#
# time.sleep(1)
# web.find_element_by_xpath('//*[@id="search_input"]').send_keys('python',Keys.ENTER)
#
# time.sleep(1)
#
# web.find_element_by_xpath('//*[@id="s_position_list"]/ul/li[1]/div[1]/div[1]/div[1]/a/h3').click()
# time.sleep(1)
# web.switch_to.window(web.window_handles[1])
#
# job_detal = web.find_element_by_xpath('//*[@id="job_detail"]/dd[2]/div').text
# print(job_detal)
#
# web.close()
# web.switch_to.window(web.window_handles[0])
#
# print(web.find_element_by_xpath('//*[@id="s_position_list"]/ul/li[1]/div[1]/div[1]/div[1]/a/h3').text)
web.get(r'https://www.91kanju.com/vod-play/541-2-1.html')
iframe = web.find_element_by_xpath('//*[@id="player_iframe"]')
web.switch_to.frame(iframe)