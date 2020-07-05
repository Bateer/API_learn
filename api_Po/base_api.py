# -*- Coding: utf-8 -*-
# Author: Yu

import requests
import json
import datetime, time
import yaml
from unit.yaml_handle import yaml_handle_cls
from jsonpath import jsonpath


# 获取应用的token
class BaseApi(object):
    url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
    corpid = "ww0ae5335f28133158"
    token_dict = dict()
    token_time = dict()
    params = {}

    @classmethod
    def format(cls, result):
        cls.r = result
        return json.dumps(json.load(result.text), indent=2, ensure_ascii=False)

    def json_path(self, path, r=None):
        if r is None:
            r = self.r
        return jsonpath(r, path)

    @classmethod
    def get_token(cls, secret):
        r = requests.get(
            url=cls.url,
            params={
                "corpid": cls.corpid,
                "corpsecret": secret
            }
        )
        print(r.text)
        token = r.json()["access_token"]
        return token

    @classmethod
    def get_access_token(cls, secret):
        if secret not in cls.token_dict.keys():
            r_token = cls.get_token(secret)
            cls.token_dict[secret] = r_token
            cls.token_dict.update()
            cls.token_time[secret] = datetime.datetime.now()
            cls.token_time.update()
            print(cls.token_dict)
        else:
            old_time = cls.token_time[secret]
            old_t = time.mktime(old_time.timetuple())
            now_time = datetime.datetime.now()
            now_t = time.mktime(now_time.timetuple())
            apart_time = now_t - old_t
            if apart_time > 7200:
                r_token = cls.get_token(secret)
                cls.token_dict[secret] = r_token
                cls.token_dict.update()
                cls.get_access_token(secret)
        return cls.token_dict[secret]

    @classmethod
    def api_load(cls, filename):
        return yaml_handle_cls.yaml_load(filename)

    @classmethod
    def replace_data(cls, data: dict):
        raw = yaml.dump(data)
        for key, value in cls.params.items():
            raw = raw.replace(f'{{{key}}}', value)
        data = yaml.load(raw)
        return data

    @classmethod
    def api_send(cls, req: dict):
        data = cls.replace_data(req)
        result = requests.request(
            method=data["method"],
            url=data["url"],
            params=data["params"]["access_token"],
            json=data.get("json")
        )
        print(result)
        # cls.format(result)
        return result

