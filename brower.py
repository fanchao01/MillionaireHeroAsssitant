#coding:utf-8

import utils
import time
from selenium import webdriver

Str2Browser = {
   'ie': 'Ie',
   'firefox': 'Firefox',
}


IE = None


@utils.timeit
def ie(key, browser='Ie', auto_close=(False, 0)):
    """
    the key is complete url including search engine
    """
    global IE
    if IE is None:
        browser = Str2Browser.get(browser.lower(), 'Ie')
        driver = getattr(webdriver, browser)()
        IE = driver
    IE.get(key)
    if auto_close[0]:
        time.sleep(auto_close[1])
        IE.quit()
        IE = None
        print 'Close browser after 20 seconds'


def quit():
    global IE
    if IE:
        IE.quit()
        IE = None


if __name__ == '__main__':
    ie('http://www.baidu.com/s?wd=\xe6\x88\x91\xe7\x9a\x84')
