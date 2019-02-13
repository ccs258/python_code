# -*- coding: utf-8 -*-
# @Time    : 19-2-13 下午8:35
# @Author  : ccs
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

_user = "it@socialcredits.cn"
_pwd = "cms.2016.2018"
_to = '1154911548@qq.com'
sender = '916367141@qq.com'
receivers = ['1154911548@qq.com']

message = MIMEMultipart()


message['From'] = Header("菜鸟教程",'utf-8')
message['To'] = Header("测试",'utf-8')
subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject,'utf-8')


####注意attach里面是MIMEText()对象
message.attach(MIMEText('这是菜鸟教程python邮件测试....','plain','utf-8'))


att1 = MIMEText(open('/home/ccs/Desktop/test.txt','rb').read(),'base64','utf-8')
att1["Content-Type"] = 'application/octet-stream'
att1['Content-Disposition'] = 'attachment;filename="text.txt"'
message.attach(att1)




#发送HTML格式
# 将数据转换为html的table
# result是list[list1,list2]这样的结构
# title是list结构；和result一一对应。titleList[0]对应resultList[0]这样的一条数据对应html表格中的一列
import pandas as pd
d = {}
index = 0
result = [[u'2016-08-25', u'2016-08-26', u'2016-08-27'], [u'张三', u'李四', u'王二']]
title = [u'日期', u'姓名']
for t in title:
    d[t] = result[index]
    index = index + 1
df = pd.DataFrame(d)
df = df[title]
h = df.to_html(index=False)
email_content = MIMEText("<h1>每日推送数据统计报告,详情请参加附件,请勿回复,谢谢!</h1>"
                             + "<h2>新设企业详情</h2>"+h,'html', 'utf-8')
message.attach(email_content)

####如果直接写，会报错，注意attach里面是实例化的MIMEText对象；
#AttributeError: 'str' object has no attribute 'policy'
# message.attach(h)

#html里面的语言教程参考：http://www.w3school.com.cn/tags/index.asp
"""
<h1>这是标题 1</h1>
<h2>这是标题 2</h2>
<h3>这是标题 3</h3>
<h4>这是标题 4</h4>
<h5>这是标题 5</h5>
<h6>这是标题 6</h6>
"""



try:
    s = smtplib.SMTP("smtp.mxhichina.com", timeout=30)  # 连接smtp邮件服务器,端口默认是25
    s.login(_user, _pwd)
    s.sendmail(_user, _to, message.as_string())
    # smtpObj = smtplib.SMTP('smtp.qq.com', 587)  ####发送邮件不成功，可能是本地邮件服务器的支持问题；
    # smtpObj.sendmail(sender,receivers,message.as_string())
    print('邮件发送成功')
except smtplib.SMTPException:
    print('Error:无法发送邮件')


"""
MIMEMultipart类用于实现多部分(支持用attach添加多种形式：附件，html，纯文本等等吧？？)邮件的功能，缺省情况下它会创建Content-Type类型为mulitpart/mixed邮件。
class MIMEMultipart(MIMEBase):
    Base class for MIME multipart/* type messages.
 
    def __init__(self, _subtype='mixed', boundary=None, _subparts=None,
                 **_params):
        Creates a multipart/* type message.
        By default, creates a multipart/mixed message, with proper
        Content-Type and MIME-Version headers.
        _subtype is the subtype of the multipart content type, defaulting to
        `mixed'.
        boundary is the multipart boundary string.  By default it is
        calculated as needed.
        
        #####attach的作用！！！！！！！！
        _subparts is a sequence of initial subparts for the payload.  It
        must be an iterable object, such as a list.  You can always
        attach new subparts to the message by using the attach() method
 #####在类初始化时，会将_payload初始化为空的列表，因为在Message超类中is_multipart方法假设_payload是一个列表，
 并用来存放多部分邮件内容，利用attach()方法可以将多部分邮件(多种格式相同或者不同的格式---MIMEText对象)添加到列表中。
 这里来看一下超类Message中的相关实现：
参考讲述smtp类调用原理的经典博客：https://blog.csdn.net/jinguangliu/article/details/45272863


########
参考：http://www.runoob.com/python/python-email.html
https://www.jianshu.com/p/abb2d6e91c1f
https://docs.python.org/2/library/email-examples.html#email-examples

html相关：https://docs.python.org/2/library/email-examples.html#email-examples
"""