# 导包
from unittest import TestCase
from requests import Response
import app
import json


def assert_utils(self, response, status_code, success, code, message):
    '''
    @type self:TestCase
    @type response:Response
    '''
    jsonData = response.json()
    self.assertEqual(status_code, response.status_code)
    self.assertEqual(success, jsonData.get("success"))
    self.assertEqual(code, jsonData.get("code"))
    self.assertEqual(message, jsonData.get("message"))


def read_login_data():
    data_path = app.BASH_DIR + "/data/login_data.json"
    with open(data_path, encoding="utf-8") as f:
        jsonData = json.load(f)
        login_data_list = []

        for login_data in jsonData:
            mobile = login_data.get("mobile")
            password = login_data.get("password")
            status_code = login_data.get("status_code")
            success = login_data.get("success")
            code = login_data.get("code")
            message = login_data.get("message")

            login_data_list.append((mobile, password, status_code, success, code, message))

        return login_data_list
