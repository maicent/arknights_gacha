# -*- coding: UTF-8 -*-
import requests
import json
import simplejson


class Arknights:
    def __init__(self, user, pwd):
        self.phone = user
        self.pwd = pwd

    def login(self):
        url = 'https://as.hypergryph.com/user/auth/v1/token_by_phone_password'
        data = {
            'phone': self.phone,
            'password': self.pwd,
        }
        re = requests.post(url, headers=header, data=data)
        return re.json()['status']

    def get_token(self):
        url = 'https://as.hypergryph.com/user/auth/v1/token_by_phone_password'
        data = {
            'phone': self.phone,
            'password': self.pwd,
        }
        re = requests.post(url, headers=header, data=data)
        return re.json()['data']['token']

    def gacha_list(self, token):
        url = 'https://ak.hypergryph.com/user/api/inquiry/gacha'
        data_total = {
            'page': 20,
            'token': token,
        }
        total = requests.get(url, headers=header, params=data_total)
        total = total.json()['data']['pagination']['total']
        page_max = int(total) // 10 + 1
        gacha_list = []
        for i in range(page_max):
            data_list = {
                'page': int(i) + 1,
                'token': token,
            }
            gacha_list_tmp = requests.get(url, headers=header, params=data_list)
            # gacha_list_tmp.json()['data']['list']
            gacha_list += gacha_list_tmp.json()['data']['list']
        with open('html/data.json', 'w', encoding='utf-8') as f:
            dic_tmp = {'data': gacha_list}
            dic = 'fn('+json.dumps(dic_tmp, ensure_ascii=False)+')'
            f.write(dic)
        return gacha_list

    @staticmethod
    def data_process(gacha_list):
        global six, five, four, three
        agent = []
        for i in range(len(gacha_list)):
            agent += gacha_list[i]['chars']
        cnt = 0
        print(agent)
        for i in agent:
            cnt += 1
            # print('第'+str(cnt)+'发：'+i['name'])
            if i['rarity'] == 5:
                i['times'] = cnt
                six.append(i)
            elif i['rarity'] == 4:
                i['times'] = cnt
                five.append(i)
            elif i['rarity'] == 3:
                i['times'] = cnt
                four.append(i)
            else:
                i['times'] = cnt
                three.append(i)

header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
        "Accepted-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept": "application/json, text/javascript, */*; q=0.01",
    }
if __name__ == '__main__':

    six = []
    five = []
    four = []
    three = []
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
        "Accepted-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept": "application/json, text/javascript, */*; q=0.01",
    }
    phone = ''
    pwd = ''
    ak = Arknights(phone, pwd)
    ak.data_process(ak.gacha_list(ak.get_token()))
    # print(six)
    # print(five)
    # print(four)
    # print(three)
