from email.mime.text import MIMEText
from email.header import Header
import smtplib
import getpass

"""
    邮件传输模块编程

"""

def inet_mail(host, sender, passwd, receivers, subject, body):
    # 准备邮件正文,plain表示纯文本
    message = MIMEText(body, 'plain', 'utf8')
    message['From'] = Header('root', 'utf8')        # 发件人
    message['To'] = Header(receivers[0], 'utf8')    # 收件人
    message['Subject'] = Header(subject, 'utf8')    # 主题

    # 发邮件
    smtp = smtplib.SMTP()
    smtp.connect(host)
    smtp.starttls() # 如果服务器要求安全连接,则打开注释
    smtp.login(sender, passwd)
    smtp.sendmail(sender, receivers, message.as_bytes())

if __name__ == '__main__':
    passwd = getpass.getpass()
    # 此处密码为qq邮箱生成的授权码,
    # 查找方式:邮箱设置>账户>POP3/IMAP/SMTP/Exchange/CardDAV/CalDAV服务

    server = 'smtp.qq.com'
    sender = 'xxx@qq.com'
    receivers = ['xxx@163.com']
    subject = 'python inet邮件测试'
    body = "这是个pycharm测试\r\n"
    inet_mail(server, sender, passwd, receivers, subject, body)
