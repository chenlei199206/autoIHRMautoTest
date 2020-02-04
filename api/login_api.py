import requests
import app


class LoginApi():
    def __init__(self):
        # 登录的url
        self.login_url = app.HOST + "/api/sys/login"
        # 登录的请求头
        self.headers = app.HERDERS

    def login(self, mobile, password):
        data = {
            "mobile": mobile,
            "password": password
        }
        return requests.post(url=self.login_url, json=data, headers=self.headers)

    def login_empty(self):
        return requests.post(url=self.login_url)

    def login_add_params(self, mobile, password, **kwargs):
        data = {
            "mobile": mobile,
            "password": password
        }

        if kwargs:
            for k, v in kwargs.items():
                data[k] = v

        return requests.post(url=self.login_url, json=data, headers=self.headers)
