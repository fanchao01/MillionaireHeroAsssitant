#coding:utf-8
import utils
import brower
import grab
import orc
import register as _register


CONF = {
    'debug': False,
    'engine': 'http://www.baidu.com/s?wd=', # @baidu search uri prifix
    'browser': 'IE', # search engine, IE, Firefox, Chrome supported,
                     # the browser and its webdriver must be installed
                     # IE starts more quickly
    'auto_close': (False, 20),   # auto close the browser after 20 seconds
    'bbox': [80, 220, 190, 315],

    # baidu orc api auth
    #'app_id':       '$app_id',
    #'api_key':      '$api_key',
    #'secret_key':   '$secret_key',
}


def register():
    _register.RegisterPy()


@utils.timeit
def go():
    image = grab.grab(bbox=CONF['bbox'])
    key = orc.orc(data=image)
    url = CONF.get('engine') + key
    brower.ie(url, CONF['browser'], CONF['auto_close'])


def quit():
    brower.quit()


def test():
    key = orc.orc(filepath='./test.jpg')
    url = CONF.get('engine') + key
    brower.ie(url, CONF['browser'], CONF['auto_close'])


def main():
    orc.get_client(CONF['app_id'], CONF['api_key'], CONF['secret_key'])
    test()

    while True:
        wds = raw_input(u'millionaire >> ')
        if wds.strip().lower().startswith('c') or not wds.strip():
            go()
        elif wds.strip().lower().startswith('q'):
            quit()
            break

if __name__ == '__main__':
    main()
