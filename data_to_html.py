# -*- coding: utf-8 -*-
# @Time    : 19-2-13 下午9:39
# @Author  : ccs
import pandas as pd


def convertToHtml(result, title):
    # 将数据转换为html的table
    # result是list[list1,list2]这样的结构
    # title是list结构；和result一一对应。titleList[0]对应resultList[0]这样的一条数据对应html表格中的一列
    d = {}
    index = 0
    for t in title:
        d[t] = result[index]
        index = index + 1
    df = pd.DataFrame(d)
    df = df[title]
    h = df.to_html(index=False)
    return h


if __name__ == '__main__':
    result = [[u'2016-08-25', u'2016-08-26', u'2016-08-27'], [u'张三', u'李四', u'王二']]
    title = [u'日期', u'姓名']
    print(convertToHtml(result, title))

"""
(1)df结果的形式：
           日期  姓名
0  2016-08-25  张三
1  2016-08-26  李四
2  2016-08-27  王二

(2)df转换成html后的形式：
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>日期</th>
      <th>姓名</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2016-08-25</td>
      <td>张三</td>
    </tr>
    <tr>
      <td>2016-08-26</td>
      <td>李四</td>
    </tr>
    <tr>
      <td>2016-08-27</td>
      <td>王二</td>
    </tr>
  </tbody>
</table>

"""