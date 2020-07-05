# -*- Coding: utf-8 -*-
# Author: Yu

import requests
from requests import Session, Response

def test_request_get():
    r = requests.get("https://httpbin.testing-studio.com/get")
    print(r.json())
    print(r.headers)
    print(r.status_code)
    assert r.status_code == 200


def test_get():
    params = {
        "a": 1,
        "b": 2,
        "c": 3
    }
    r = requests.get(
        "https://httpbin.testing-studio.com/get",
        params=params)
    print(r.json())


def test_post():
    params = {
        "a": 4,
        "b": 5,
        "c": 6
    }
    data = {
        "a": "a",
        "b": "b",
        "c": "ccccc"
    }
    r = requests.post(
        "https://httpbin.testing-studio.com/post",
        params=params,
        data=data
    )
    print(r.json())
    print(r.status_code)


def test_upload():
    r = requests.post(
        "https://httpbin.testing-studio.com/post",
        files={"file": open("file.py", "rb")}
    )
    print(r.json())


def test_get_hook():
    def modify_response(r: Response, *args, **kwargs):
        # r.text = "HELLO THIS MY HOOK!"
        r.expend = "HELLO THIS MY HOOK!"
        r.url = "this nmy"
        return r
    r = requests.post(
        "https://httpbin.testing-studio.com/post",
        data={
            "a": 1,
            "b": 2
        },
        hooks={"response": [modify_response]}
    )
    print(r.text)
    print(r.expend)
    print(r.url)
