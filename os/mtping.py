import subprocess
import threading

"""
    多线程threading应用: 扫描网段存活主机
    patch: 用面向对象的编写方式实现

"""
class Ping:
# 定义Ping类
    def __init__(self, host):
        self.host = host

    def __call__(self):
    # 利用__call__方法让Ping类可以生成调用的对象
        result = subprocess.run(
            'ping -c2 %s &> /dev/null' % self.host, shell=True
            # 调用系统模块subprocess,执行系统命令,指定命令是shell
        )

        if result.returncode == 0:
        # 判断系统命令退出码,成功为0,不成功为非0
            print('%s:up' % self.host)
        else:
            print('%s:down' % self.host)


if __name__ == '__main__':
    ips = ('xxx.xxx.xxx.%s' % i for i in range(1, 255))
    # 利用列表解析生成ip,存入序列中
    for ip in ips:
        t = threading.Thread(target=Ping(ip))
        # 创建实例
        t.start()
        # 等同于target() 调用实例