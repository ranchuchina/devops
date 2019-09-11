from urllib import request, error
import wget
import os
import re

def download(url, fname):
    html = request.urlopen(url)
    with open(fname, 'wb') as fobj:
        while True:
            data = html.read(4096)
            if not data:
                break
            fobj.write(data)

if __name__ == '__main__':
    dest = '/tmp/163'
    # 设置文件路径
    fname163 = '/tmp/163/163.html'
    # 设置文件名
    if not os.path.exists(dest):
    # 判断文件是否存在,不存在则创建
        os.makedirs(dest)
    if not os.path.exists(fname163):
    # 判断文件是否存在,不存在则下载
        download('http://www.163.com', fname163)
    # 获取图片URL
    url_patt = '(http|https)://[-./\w]+\.(png|jpg|jpeg|gif)'
    img_urls = []  # 用于存储图片的网址
    patt = re.compile(url_patt)
    # 将正则表达式字符串形式变异为patt实例
    with open(fname163, encoding='gbk') as fobj:
        for line in fobj:
            m = patt.search(line)
            # 使用patt实例查找匹配规则的网址
            if m:
                img_urls.append(m.group())
                # 将匹配到的图片网址追加到result列表
    for url in img_urls:
        try:
            wget.download(url, dest)
        except error.HTTPError:
            pass
