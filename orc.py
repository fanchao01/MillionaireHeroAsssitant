# coding: utf-8
import utils

from aip import AipOcr

Client = None


def strip(s):
    print s
    na = u'哪'
    if na in s:
        i = s.find(na)
        s = s[:i] + s[i+2:]

    words = [u'1', u'2', u'3', u'4', u'5', u'6', u'7', u'8', u'9', u'10', u'11', u'12', u'以下', u'?', u'？', u'.', u'。']

    for w in words:
        if w in s:
            i = s.find(w)
            s = s[:i] + s[i+len(w):]

    return s


def get_client(app_id=None, api_key=None, secret_key=None):
    global Client
    if Client: 
        return Client

    Client = AipOcr(app_id, api_key, secret_key)
    return Client


@utils.timeit
def orc(filepath=None, data=None, client=None):
    client = client or get_client()

    if filepath:
        with open(filepath, 'rb') as fp:
            data = fp.read()

    response = client.basicGeneral(data)

    s = u' '.join([w['words'].strip() for w in response['words_result'] if w.get('words', None)])
    return strip(s).encode('utf8')


if __name__ == '__main__':
    client = get_client(app_id='', api_key='', secret_key='')
    print orc('./test.JPG', client=client)
