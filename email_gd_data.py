# -*- coding: utf-8 -*-
# @Time    : 19-2-13 下午10:02
# @Author  : ccs
# encoding=utf-8
import smtplib


from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import pandas as pd

_user = "xx"
_pwd = "xx"
_to = ["115491154@qq.com"]


# _to = ["yong.bai@socialcredits.cn"]

"""
区分：/usr/lib/python3.5/email/message.py ----
  def attach(self, payload):
     Add the given payload to the current payload.
        The current payload will always be a list of objects after this method
        is called.  If you want to set the payload to a scalar object, use
        set_payload() instead.


与/home/ccs/PycharmProjects/untitled/venv/lib/python3.5/site-packages/django/core/mail/message.py
    def attach(self, filename=None, content=None, mimetype=None):

        Attach a file with the given filename and content. The filename can
        be omitted and the mimetype is guessed, if not provided.

        If the first parameter is a MIMEBase subclass, insert it directly
        into the resulting message attachments.

        For a text/* mimetype (guessed or specified), when a bytes object is
        specified as content, decode it as UTF-8. If that fails, set the
        mimetype to DEFAULT_ATTACHMENT_MIME_TYPE and don't decode the content.

"""

def send_mail(file, file_name, all_count_list, es_data_list):
    # 如名字所示Multipart就是分多个部分
    msg = MIMEMultipart()

    msg["Subject"] = "每日推送数据统计报告".encode('utf-8')
    msg["From"] = _user
    msg["To"] = ", ".join(_to)  # 支持发给多人

    # 正文
    # part = MIMEText("每日推送数据统计报告,详情请参加附件,请勿回复,谢谢!",'plain', 'utf-8')
    # msg.attach(part)

    clear_result = clear_data_table(all_count_list)
    try:
        es_data_clear_result = clear_data_table(es_data_list[0])
    except BaseException:
        es_data_clear_result = ''
    all_data_table = table_data_2html(
        clear_result, [
            u"表名", u"表备注", u"提供数据数据", u"存在有字段异常的条数", u"提供的日期"])
    es_data_table = table_data_2html(
        es_data_clear_result, [
            u"表名", u"表备注", u"企业注册日期", u"企业数量", u"提供的日期"])
    email_content = MIMEText("<h3>每日推送数据统计报告,详情请参加附件,请勿回复,谢谢!</h3>"
                             + "<h4>新设企业详情</h4>"
                             + es_data_table
                             + "<h4>按表统计</h4>"
                             + all_data_table,
                             'html', 'utf-8')
    msg.attach(email_content)
    # xlsx类型附件
    try:
        part = MIMEApplication(open(file, 'rb').read())
        part.add_header(
            'Content-Disposition',
            'attachment',
            filename=file_name)
        msg.attach(part)
    except BaseException:
        part = MIMEText("报告生成失败,请检查程序", 'plain', 'utf-8')
        msg.attach(part)

    s = smtplib.SMTP("smtp.mxhichina.com", timeout=30)  # 连接smtp邮件服务器,端口默认是25
    s.login(_user, _pwd)
    s.sendmail(_user, _to, msg.as_string())
    s.close()


def clear_data_table(all_count_list):
    # 整理表格字段
    name_list = []
    note_list = []
    data_list = []
    error_list = []
    date_list = []
    for v in all_count_list:
        name_list.append(v[0])
        note_list.append(v[1])
        data_list.append(v[2])
        error_list.append(v[3])
        date_list.append(v[4])
    return [name_list, note_list, data_list, error_list, date_list]


def table_data_2html(result, title):
    # 将数据转换为html的table
    # result是list[list1,list2]这样的结构
    d = {}
    index = 0
    for t in title:
        d[t] = result[index]
        index = index + 1
    df = pd.DataFrame(d)
    df = df[title]
    h = df.to_html(index=False)
    return h

