# 县及县以上行政区划代码

[![Join the chat at https://gitter.im/cn/GB2260](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/cn/GB2260)
[![GB/T 2260](http://img.shields.io/badge/GB%2FT-2260-blue.svg?style=flat)](spec.md)

中华人民共和国国家标准 GB/T 2260 行政区划代码

数据来源：

1. <http://www.stats.gov.cn/tjsj/tjbz/xzqhdm/>
2. <http://www.mca.gov.cn/article/sj/tjbz/a/>

你可以利用国家标准数据构建自己项目的数据库。



# 身份证校验器功能（此身份证校验器的源代码是shenfenzheng.py）
1.不仅仅可以校验最新的行政区划，之前存在的数据都已存入一起校验；
2.通过身份证最后一位的校验码，可以校验此身份证的有效性；
3.根据身份证倒数第二位可以得出性别；
4.根据身份证信息得出出生年月；
5.根据身份证前六位得出此身份证详细的办证地点；
6.此校验器已完成15位和18位身份证的同时使用；
7.当校验器工作时，每当身份证中有错误的地方都提示相应问题，并且会停止其它校验。

# 此校验器的运行
下载mca文件夹中的行政区划代码和校验器源代码即可运行！
 
