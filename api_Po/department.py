# -*- Coding: utf-8 -*-
# Author: Yu
import requests
from api_Po.base_api import BaseApi


class Department_po(BaseApi):
    secret = "1ZGHhpKHOEhewTMTTyHOEi5uKkLXM3Bhkvfjl2ELU3s"

    @classmethod
    def get_department_token(cls):
        department_token = BaseApi.get_access_token(cls.secret)
        return department_token

    @classmethod
    def creat_department(cls, name, parentid, *args, **kwargs):
        # url = "https://qyapi.weixin.qq.com/cgi-bin/department/create"
        # access_token = cls.get_department_token()
        # params = {"access_token": access_token}
        # json = {
        #     "name": name,
        #     "parentid": parentid
        # }
        # json.update(*args, **kwargs)
        # r = requests.post(
        #     url=url,
        #     params=params,
        #     json=json
        # )
        access_token = cls.get_department_token()
        cls.params["access_token"] = access_token
        data = cls.api_load("department.api.yaml")
        replace_req = cls.replace_data(data["creat_department"])
        print("------------", replace_req)
        r = cls.api_send(replace_req)
        return r.json()

    @classmethod
    def update_department(cls, id, *args, **kwargs):
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/update"
        access_token = cls.get_department_token()
        params = {"access_token": access_token}
        json = {
            "id": id
        }
        json.update(*args, **kwargs)
        r = requests.post(
            url=url,
            params=params,
            json=json
        )
        return r.json()

    @classmethod
    def del_department(cls, id):
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/delete"
        access_token = cls.get_department_token()
        params = {
            "access_token": access_token,
            "id": id
        }
        r = requests.get(
            url=url,
            params=params
        )
        return r.json()

    @classmethod
    def list_department(cls, *args, **kwargs):
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/list"
        access_token = cls.get_department_token()
        params = {
            "access_token": access_token
        }
        params.update(*args, **kwargs)
        r = requests.get(
            url=url,
            params=params
        )
        return r.json()