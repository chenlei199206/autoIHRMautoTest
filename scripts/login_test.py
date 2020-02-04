# 导包
import unittest
from api.login_api import LoginApi
import logging
from utils import assert_utils


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.login_api = LoginApi()

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test01_login_success(self):
        # 发送登录请求
        respose = self.login_api.login("13800000002", "123456")
        logging.info("登录成功的数据 : {}".format(respose.json()))
        #
        # json_data = respose.json()
        # self.assertEqual(200,respose.status_code)
        # self.assertEqual(True,json_data.get("success"))
        # self.assertEqual(10000, json_data.get("code"))
        # self.assertEqual("操作成功！", json_data.get("message"))

        assert_utils(self, respose, 200, True, 10000, "操作成功！")

    #手机号不存在
    def test02_mobile_not_exits(self):
        respose = self.login_api.login("13800001002", "123456")
        logging.info("手机号不存在 : {}".format(respose.json()))
        assert_utils(self, respose, 200, False, 20001, "用户名或密码错误")

    #密码错误
    def test03_password_error(self):
        respose = self.login_api.login("13800000002", "error")
        logging.info("密码错误 : {}".format(respose.json()))
        assert_utils(self, respose, 200, False, 20001, "用户名或密码错误")

    #参数为空
    def test04_params_null(self):
        respose = self.login_api.login_empty()
        logging.info("参数为空 : {}".format(respose.json()))
        assert_utils(self, respose, 200, False, 99999, "抱歉，系统繁忙，请稍后重试！")

    #用户名为空
    def test05_mobile_null(self):
        respose = self.login_api.login("", "123456")
        logging.info("用户名为空 : {}".format(respose.json()))
        assert_utils(self, respose, 200, False, 20001, "用户名或密码错误")

    #密码为空
    def test06_password_null(self):
        respose = self.login_api.login("13800000002", "")
        logging.info("密码为空 : {}".format(respose.json()))
        assert_utils(self, respose, 200, False, 20001, "用户名或密码错误")

    #多参
    def test07_params_add(self):
        respose = self.login_api.login_add_params("13800000002", "123456", addparams="heihei")
        logging.info("多参 : {}".format(respose.json()))
        assert_utils(self, respose, 200, True, 10000, "操作成功！")

