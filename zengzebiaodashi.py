#coding=utf-8
import re
import requests
#match:从起始位置开始匹配，否则返回None
'''content='Hello 1234567 is a number.Regex String'
content2=''Hello is a number. 
           Regex String 1234567''
#result=re.match('^Hello (\d+).*String$',content)#^Hello:匹配字符串开头；(\d+)匹配任意个数字；.*匹配任一字符（换行符除外)
#贪婪模式
result=re.match('.*(\d+).*',content)#'.*':可以匹配所有字符
result1=re.match('.*?(\d+).*',content2,flags=re.S)

#非贪婪模式
result2=re.match('.*?(\d+).*',content)

#*String匹配字符串结尾
if result1:
    print (result1.group(1))#取出第一个括号的内容

if result2:
    print(result2.group(1))
'''

#search扫描整个字符串并返回第一个成功的匹配
'''content='Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
ma_result=re.match('Hello.*?(/d+).*?Demo',content)
se_result=re.search("Hello.*?(\d+).*?Demo",content)
if True:
    print(ma_result)
    print(se_result.group(1))
'''

#re.findall() 搜索字符串，以列表形式返回全部能匹配的字串
# 取出html中的歌手名和歌名
html = '''<div id="songs-list">
    <h2 class="title">经典老歌</h2>
    <p class="introduction">
        经典老歌列表
    </p>
    <ul id="list" class="list-group">
        <li data-view="2">一路上有你</li>
        <li data-view="7">
            <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
        </li>
        <li data-view="4" class="active">
            <a href="/3.mp3" singer="齐秦">往事随风</a>
        </li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
        <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
        <li data-view="5">
            <a href="/6.mp3" singer="邓丽君">但愿人长久</a>
        </li>
    </ul>
</div>'''
find_result=re.findall('<a.*?singer="(.*?)">(.*?)</a>',html)
if find_result:
    print(find_result)


#爬虫实战练习
content=requests.get("https://movie.douban.com/chart").text
pattern=re.compile('class="pl2".*?<.*?="(.*?)".*?>(.*?)<span.*?>(.*?)</span>.*?"rating_nums">(.*?)</span>.*?"pl">(.*?)</span>', re.S)
results=re.findall(pattern,content)
for result in results:
    url,name1,name2,nums,pl=result
    print(url,name1.replace("/","").strip(),name2.replace("/","").strip(),nums,pl)