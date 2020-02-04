# 导包
import time
import unittest
from scripts.login_test import LoginTest
from tools.HTMLTestRunner import HTMLTestRunner
import app

# 生成测试套件
suite = unittest.TestSuite()
# 组装测试套件
suite.addTest(unittest.makeSuite(LoginTest))
# 指定测试报告的地址和格式
# report_path = app.BASH_DIR + "/report/ihrm-{}.html".format(time.strftime("%Y%m%d %H%M%S"))
report_path = app.BASH_DIR + "/report/ihrm.html"

# 运行测试套件
with open(report_path, "wb")as f:
    runner = HTMLTestRunner(f, verbosity=1, title="IHRM人力", description="V1.21")
    runner.run(suite)
