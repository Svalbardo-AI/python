import urllib.request



def getUrlRespHtml(url):
    heads = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
             'Accept-Charset': 'GB2312,utf-8;q=0.7,*;q=0.7',
             'Accept-Language': 'zh-cn,zh;q=0.5',
             'Cache-Control': 'max-age=0',
             'Connection': 'keep-alive',
             'Host': 'John',
             'Keep-Alive': '115',
             'Referer': url,
    'User-Agent': 'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.14) Gecko/20110221 Ubuntu/10.10 (maverick) Firefox/3.6.14'}

    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor())
    urllib.request.install_opener(opener)
    req = urllib.request.Request(url)
    opener.addheaders = heads.items()
    respHtml = opener.open(req).read()
    try:
        return respHtml.decode('gbk').encode('utf-8')
    except UnicodeDecodeError as e:
        return respHtml.decode('utf-8')
    else:
        print('Nothing right')

a=input('enter the url:')
a=getUrlRespHtml(r'http://'+a)
print(a)