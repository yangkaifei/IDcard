//字段值为中文、空格、特殊符号的地方需要做urlencode，编码为utf-8。用js的方式就是：
//encodeURIComponent('中文')
//比如"中文"转换后就是%25E4%25B8%25AD%25E6%2596%2587
curl   "http://route.showapi.com/64-19?showapi_appid=47603&showapi_timestamp=20151214132239&showapi_sign=ca914b5e520c4d6cb4aeb23415e8e057&com=auto&nu=968018776110&"
