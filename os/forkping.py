import subprocess   # 系统命令模块
import os      # fork()函数依赖模块


"""
    多进程应用fork(): 扫描网段存活主机

"""


def ping(host):
    result = subprocess.run(
        'ping -c2 %s &> /dev/null' % host, shell=True
        # 调用系统命令模块,执行ping命令
    )

    if result.returncode == 0:
    # 判断系统命令执行完成后退出的返回值,成功为0,不成功为非0
        print('%s:up' % host)
    else:
        print('%s:down' % host)

if __name__ == '__main__':
    ips = ('xxx.xxx.xxx.%s' % i for i in range(1, 255))
    for ip in ips:
    # 通过遍历列表方式循环获取ip地址,并且传参给ping()函数调用
        retval = os.fork()
        # 变量retval接收fork函数的返回值
        if not retval:
        # 通过fork返回的值来判断当前进程是子进程还是父进程,并调用ping函数
            ping(ip)
            exit()