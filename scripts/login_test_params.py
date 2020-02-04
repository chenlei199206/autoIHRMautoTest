# 导包
import unittest
from api.login_api import LoginApi
import logging
from utils import assert_utils, read_login_data
from parameterized.parameterized import parameterized


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.login_api = LoginApi()

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    @parameterized.expand(read_login_data)
    def test01_login(self, mobile, password, status_code, success, code, message):
        # 发送登录请求
        respose = self.login_api.login(mobile, password)
        logging.info("登录成功的数据 : {}".format(respose.json()))
        assert_utils(self, respose, status_code, success, code, message)

    # 参数为空
    def test04_params_null(self):
        respose = self.login_api.login_empty()
        logging.info("参数为空 : {}".format(respose.json()))
        assert_utils(self, respose, 200, False, 99999, "抱歉，系统繁忙，请稍后重试！")

    # 多参
    def test07_params_add(self):
        respose = self.login_api.login_add_params("13800000002", "123456", addparams="heihei")
        logging.info("多参 : {}".format(respose.json()))
        assert_utils(self, respose, 200, True, 10000, "操作成功！")
