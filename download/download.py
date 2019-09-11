import sys  # 位置系统模块
from urllib import request # urllib模块


def download(url, fname):
# 定义函数,函数需要两个参数,一个是下载连接,一个是文件名
    html = request.urlopen(url)
    # 打开网页
    with open(fname, 'wb') as fobj:
    # 以二进制,写方式打开文件,如果存在则清空,布存在则创建
        while True:
        # 循环读取数据
            data = html.read(4096)
            # 读取数据,每次4096,赋予变量接受
            if not data:
            # 判断循环停止条件
                break
            fobj.write(data)
            # 写入数据到文件


if __name__ == '__main__':
    download(sys.argv[1], sys.argv[2])
    # 调用函数,需要在函数文件后加2个位置参数