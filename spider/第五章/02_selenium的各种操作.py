from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time

web =Chrome()
web.get('http://lagou.com')
el = web.find_element_by_xpath('//*[@id="changeCityBox"]/p[1]/a')
el.click()

time.sleep(1)


web.find_element_by_xpath('//*[@id="search_input"]').send_keys('python',Keys.ENTER)

time.sleep(1)

li_list=web.find_elements_by_xpath('//*[@id="s_position_list"]/ul/li')

for li in li_list:
    job_name = li.find_element_by_tag_name('h3').text
    job_price = li.find_element_by_xpath('./div/div/div[2]/div/span').text
    company_name = li.find_element_by_xpath('./div/div[2]/div').text
    print(job_name,job_price,company_name)