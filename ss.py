#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import base64
import requests
from bs4 import BeautifulSoup


def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0(Macintosh; Intel Mac OS X 10_11_4)\
		AppleWebkit/537.36(KHTML, like Gecko) Chrome/52 .0.2743. 116 Safari/537.36'
    }  # 模拟浏览器访问
    response = requests.get(url, headers=headers)  # 请求访问的网页链接
    html = response.text  # 获取网页源码
    return html				# 返回网页源码


url = 'https://github.com/Alvin9999/new-pac/wiki/ss免费账号'
soup = BeautifulSoup(get_html(url), 'lxml')  # 初始化 BeautifulSoup 库，并设置解析器

list = []
configs_ss = []
configs_ssr = []
for tbody in soup.find_all(name='tbody'):
    for tr in tbody.find_all(name='tr'):
        if(len(tr.find_all(name='td')) == 0):
            continue
        list.append([])
        for td in tr.find_all(name='td'):
            if td.string:
                list[-1].append(td.string)
            else:
                list[-1].append('')

for one in list:
    if one[4] == 'aes-256-gcm':
        configs_ssr.append({
            "enable": True,
            "password": " ".join(one[3].split()),
            "method": one[4].lower(),
            "remarks": one[0],
            "server": one[1],
            "obfs": one[6],
            "protocol": one[5],
            "server_port": int(one[2]),
            "remarks_base64": base64.b64encode(one[0].encode('utf-8')).decode('utf-8')
        })
    else:
        configs_ss.append({
            "enable": True,
            "password": " ".join(one[3].split()),
            "method": one[4].lower(),
            "remarks": one[0],
            "server": one[1],
            "obfs": one[6],
            "protocol": one[5],
            "server_port": int(one[2]),
            "remarks_base64": base64.b64encode(one[0].encode('utf-8')).decode('utf-8')
        })

export_ss = {
    "random": False,
    "authPass": None,
    "useOnlinePac": False,
    "TTL": 0,
    "global": False,
    "reconnectTimes": 3,
    "index": 0,
    "proxyType": 0,
    "proxyHost": None,
    "authUser": None,
    "proxyAuthPass": None,
    "isDefault": False,
    "pacUrl": None,
    "configs": configs_ss,
    "proxyPort": 0,
    "randomAlgorithm": 0,
    "proxyEnable": False,
    "enabled": True,
    "autoban": False,
    "proxyAuthUser": None,
    "shareOverLan": False,
    "localPort": 1080
}
export_ssr = {
    "random": False,
    "authPass": None,
    "useOnlinePac": False,
    "TTL": 0,
    "global": False,
    "reconnectTimes": 3,
    "index": 0,
    "proxyType": 0,
    "proxyHost": None,
    "authUser": None,
    "proxyAuthPass": None,
    "isDefault": False,
    "pacUrl": None,
    "configs": configs_ssr,
    "proxyPort": 0,
    "randomAlgorithm": 0,
    "proxyEnable": False,
    "enabled": True,
    "autoban": False,
    "proxyAuthUser": None,
    "shareOverLan": False,
    "localPort": 1080
}

with open('export_ss.json', 'w', encoding='utf-8') as f:
    json.dump(export_ss, f, ensure_ascii=False)
with open('export_ssr.json', 'w', encoding='utf-8') as f:
    json.dump(export_ssr, f, ensure_ascii=False)
