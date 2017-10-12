# -*- coding:utf-8 -*-
import urlparse
import urllib

print('send data....')
showapi_appid="47650"#替换此值
showapi_sign="7adc2cb78dc1497daf6212184a827efe"#替换此值
url="http://route.showapi.com/64-19"
send_data = urllib.urlencode({
'showapi_appid':showapi_appid.encode('utf-8')
,'showapi_sign': showapi_sign
,'com':""
,'nu':""}
)
tp=('http','route.showapi.com','/64-19','',send_data,'')
url = urlparse.urlunparse(tp)
print url
