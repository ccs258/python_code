# -*- coding: utf-8 -*-
# @Time    : 19-1-24 下午9:35
# @Author  : ccs
import json

from django.http import HttpResponse


def calc(request):
    a = request.GET['a']
    b = request.GET['b']
    c = request.GET['c']
    print(a,b,c)
    m = a+b+c
    n = b+a
    rets = {"m":m,"n":n}
    retsj = json.dumps(rets)
    return HttpResponse(retsj)

