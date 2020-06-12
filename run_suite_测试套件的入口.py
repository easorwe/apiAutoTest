# 生成测试报告时，要先执行测试用例
# 我们可以把测试用例添加到测试套件中，然后执行测试套件生成的测试报告

# 导包
import os
import unittest
import HTMLTestRunner_PY3

from script_测试用例脚本.test_work_script import TestTpshopWork
import time

# 定位当前的目录项目
base_dir = os.path.dirname(os.path.abspath(__file__))

# 创建测试套件
suite = unittest.TestSuite()
# 将测试用例添加到测试套件
suite.addTest(unittest.makeSuite(TestTpshopWork))
# 定义测试报告的目录和报告名称
report_path = base_dir + "/report_测试报告/tpshop{}.html".format(time.strftime("%Y%m%d%H%M%S"))
# 使用HTMLTestRunner_PY3生成测试报告
with open(report_path,mode="wb") as f:
# 实例化
    runner = HTMLTestRunner_PY3.HTMLTestRunner(f,verbosity=1,title="tpshop登录接口功能测试",
                                               description="这是一个更加美观的报告，前提是连上互联网")
# 使用实例化的runner运行测试套件,生成测试报告
    runner.run(suite)