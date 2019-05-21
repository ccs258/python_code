import re
def strQ2B(ustring):
    """全角转半角"""
    rstring = ""
    if not is_none(ustring):
        for uchar in ustring:
            inside_code = ord(uchar)
            # 全角空格直接转换
            if inside_code == 12288:
                inside_code = 32
            # 全角字符（除空格）根据关系转化
            elif 65374 >= inside_code >= 65281:
                inside_code -= 65248

            rstring += unichr(inside_code)
    return rstring

def address_del(x):

    if re.match(r'[a-zA-Z0-9-]{1,}$',x):
        return 'illegal'
    elif x in[u'同上',u'[档案缺失]']:
        return 'illegal'
    elif re.search(r'[~!@#$%\^&\*\-_=+<>,;:、。?/\\|～＠＃￥％＾＆＊＿＝＋＜＞，．。；：？／＼｜【】"]', x):
        return 'illegal'
    elif re.match(r'(["|\s|\t]{1,}$)', x):
        x = x.replace(' ','')
        return x
    else:
        return x

k = address_del('远市清城区东城街道长埔下长村委会辖区内奔宝达二手车综合市场I08-1商铺')
print(address_del('珠海市香洲区洲山路6号格力捌号五、六层'))
print(address_del('广东省广州市天河区天河路208号粤海天河城大厦35楼01、02A、07B、08房'))
print(address_del('远市清城区东城街道长埔下长村委会辖区内奔宝达二手车综合市场I08-1商铺'))

