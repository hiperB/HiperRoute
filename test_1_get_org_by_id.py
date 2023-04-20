#from datetime import datetime
from datetime import datetime

import requests
from bs4 import BeautifulSoup

log_level = 2  # 0 | 1 | 2
dir_logs = '/var/log/scripts'
log_file = 'test_1_get_org_by_id.log'

example_url = 'https://yandex.ru/maps/org/'
dir_html = '/opt/tmp/'

def logging(ll, text_log):
    if log_level > ll:
        lf.write(datetime.now().strftime("%c") + ' | '+ text_log +' \n')

def range_curl (start, stop):
    for id in range(start, stop):
        url = example_url + str(id)
        logging(0, "Try curl: " + url)
        page = requests.get(url)
        print(str(id) + " : " + page.status_code)
        soup = BeautifulSoup(page.content, 'html.parser')
        with open(dir_html + id + '.html', 'wb+') as f:
            f.write(soup.prettify())
            f.close()

lf = open(dir_logs+'/'+log_file, 'at')

#start
logging(0, "/-------------------------------------")
logging(0, "Started scripts")

range_curl(1, 10000)
range_curl(100000000, 100010000)
range_curl(100000000000, 100000010000)

logging(0, "Finished")
lf.close()