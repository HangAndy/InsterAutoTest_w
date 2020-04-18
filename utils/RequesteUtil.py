# -*-coding:utf-8-*-

import requests


class Requests:
    def request_api(self, url,data=None, json=None, headers=None, method="get"):
        if method == "get":
            r = requests.get(url, headers=headers)
        elif method == "post":
            r = requests.post(url,data=data, json=json, headers=headers)

        try:
            body = r.json()
        except Exception as e:
            body = r.text
        res = dict()
        code = r.status_code
        res["code"] = code
        res["body"] = body

        # ·µ»Ø×Öµä
        return res

    def get(self, url, **kwargs):
        return self.request_api(url, method='get', **kwargs)

    def post(self, url, **kwargs):
        return self.request_api(url, method='post', **kwargs)
