# my-spider-learning-by-python
This is yu-hanyang's spider-learning
---
selenium被查到的解决方案
option = Options()
option.add_argument('--disable-blink-features=AutomationControlled')
option.add_experimental_option("detach", True)

web = Chrome(options=option)
