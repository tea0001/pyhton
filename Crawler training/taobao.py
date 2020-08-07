# -*- coding = utf-8 -*-
# @Time : 2020/8/4 16:48
# @Author : 姚远
# @File : taobao.py
# @Software: PyCharm
import urllib.request
import urllib.response
import  urllib.error
import re

url = "http://s.taobao.com/search?initiative_id=tbindexz_20170306&ie=utf8&spm=a21bo.2017.201856-taobao-item.2&sourceId=tb.index&search_type=item&ssid=s5-e&commend=all&imgfile=&q=nike%E5%AE%98%E6%96%B9%E6%97%97%E8%88%B0%E5%BA%97&suggest=0_1&_input_charset=utf-8&wq=nike&suggest_query=nike&source=suggest&cps=yes&cat=50470026"
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "cookie": "thw=cn; cna=dNKeFz4ZpQwCAWdVkJpx9vaL; t=a1c099858861e2df45cbf8e426bd10ac; _m_h5_tk=75ea62456d6887c85341d0285d67b4f0_1596539583895; _m_h5_tk_enc=ecede2f03269c1a328317cc5eca89e11; cookie2=1daf0291e8c5589ac0e736c00c5cd583; v=0; _tb_token_=be3e087e3635; _samesite_flag_=true; sgcookie=E8xbE9p4NeMcJvbIcKn2U; unb=3019453352; uc3=id2=UNDVe7pnO9adUg%3D%3D&nk2=F6k3HMt3fYoEvpymOQ0YmBl9VgY%3D&lg2=WqG3DMC9VAQiUQ%3D%3D&vt3=F8dBxG2hmjxHccU%2Fekg%3D; csg=710fa087; lgc=t_1492265181596_0363; cookie17=UNDVe7pnO9adUg%3D%3D; dnk=t_1492265181596_0363; skt=57f827305f03e376; existShop=MTU5NjUzMDYyMA%3D%3D; uc4=id4=0%40UgclFl6PWRLz8AjJYkwUMDNz0wtj&nk4=0%40FbMocp0QQ%2B3RLdVm5G%2BKJhb94DhWDVGbM%2BUyU%2BtjlA%3D%3D; tracknick=t_1492265181596_0363; _cc_=WqG3DMC9EA%3D%3D; _l_g_=Ug%3D%3D; sg=329; _nk_=t_1492265181596_0363; cookie1=BxUHS1uiwKxlcyH1jN9Mz2Z2TXD7WNxomROmKSwD9Zg%3D; mt=ci=19_1; uc1=cookie14=UoTV6h5fHZcC5w%3D%3D&pas=0&cookie15=URm48syIIVrSKA%3D%3D&cookie21=U%2BGCWk%2F7p4mBoUyS4E9C&existShop=false&cookie16=UIHiLt3xCS3yM2h4eKHS9lpEOw%3D%3D; enc=Y%2F7OUY7Wq1PiJmRJyUjmW3B6%2BBrFcx3Xz1Ok6tnfVdi4mLCH8thvq3MDkH4mftZVI2IBVWbO5EPupmY6yAuFAg%3D%3D; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; hng=CN%7Czh-CN%7CCNY%7C156; JSESSIONID=689E36FB26887D05275785C4D7CFA354; l=eBNvSy8qONakISv-BOfwourza77OSIRAguPzaNbMiOCP9_5p5JeVWZos1ZY9C3GVh6bwR35e4jE9BeYBqHKKnxv92j-la_kmn; tfstk=cmZdB9c251fnTDDT3yQiNK1DtJXGZI_KZ1c22TvA5LrOcA-Riwr0DrgDjxdKXOC..; isg=BM3NGQVJroXbsAqYXq5QAWm33OlHqgF8eLaKFw9SCWTTBu241_oRTBufdJpgxhk0",
    "referer": "https://www.taobao.com/",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
}
request = urllib.request.Request(url=url, headers=headers)
try:
    response = urllib.request.urlopen(request)
    print(response.read().decode('utf-8'))
except urllib.error.URLError as e:
    if hasattr(e, "code"):
        print(e.code)
    elif hasattr(e, "reason"):
        print(e.reason)

