from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
import time

opt = Options()
opt.add_argument('--headless')
opt.add_argument('--disable-gpu')

web=Chrome(options=opt)
web.get('https://www.endata.com.cn/BoxOffice/BO/Year/index.html')

sel_el = web.find_element_by_xpath('//*[@id="OptionDate"]')
sel = Select(sel_el)
for i in range(len(sel.options)):
    sel.select_by_index(i)
    time.sleep(2)
    table = web.find_element_by_xpath('//*[@id="TableList"]/table/tbody').text
    print(table)
    print('==================================')

web.close()
print('finshed')