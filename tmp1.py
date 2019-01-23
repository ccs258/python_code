# -*- coding: utf-8 -*-
# @Time    : 19-1-17 下午11:01
# @Author  : ccs
#下载公告 参考：https://github.com/startprogress/China_stock_announcement/blob/master/python_scraw/cninfo_main.py
import datetime
from redis._compat import basestring

def list_or_args(keys, args):
    # returns a single new list combining keys and args
    try:
        iter(keys)
        # a string or bytes instance can be iterated, but indicates
        # keys wasn't passed as a list
        if isinstance(keys, (basestring, bytes)):
            keys = [keys]
        else:
            keys = list(keys)
    except TypeError:
        keys = [keys]
    if args:
        keys.extend(args)
    return keys


def timestamp_to_datetime(response):
    "Converts a unix timestamp to a Python datetime object"
    if not response:
        return None
    try:
        response = int(response)
    except ValueError:
        return None
    return datetime.datetime.fromtimestamp(response)


def string_keys_to_dict(key_string, callback):
    return dict.fromkeys(key_string.split(), callback)


def dict_merge(*dicts):
    merged = {}
    for d in dicts:
        merged.update(d)
    return merged
"""
 def update(self, E=None, **F): # known special case of dict.update
    D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
    If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
    If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
    In either case, this is followed by: for k in F:  D[k] = F[k]
    pass
"""

a = dict_merge({'a':1},{'b':3})
print(a)
#将两个小字典合成一个大字典；

def parse_sentinel_state(item):
    result = {}
    flags = set(result['flags'].split(','))
    for name, flag in (('is_master', 'master'), ('is_slave', 'slave'),
                       ('is_sdown', 's_down'), ('is_odown', 'o_down'),
                       ('is_sentinel', 'sentinel'),
                       ('is_disconnected', 'disconnected'),
                       ('is_master_down', 'master_down')):
        result[name] = flag in flags
    return result
###注意上面迭代的对象；


def float_or_none(response):
    if response is None:
        return None
    return float(response)


def parse_config_get(response, **options):
    response = [nativestr(i) if i is not None else None for i in response]
    return response and pairs_to_dict(response) or {}


def parse_slowlog_get(response, **options):
    return [{
        'id': item[0],
        'start_time': int(item[1]),
        'duration': int(item[2]),
        'command': b' '.join(item[3])
    } for item in response]

{'GEOHASH': lambda r: list(map(nativestr, r)),
'GEOPOS': lambda r: list(map(lambda ll: (float(ll[0]),
                                         float(ll[1]))
                                         if ll is not None else None, r))}

