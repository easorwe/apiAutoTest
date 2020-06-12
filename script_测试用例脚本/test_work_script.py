# 导包
import requests
import unittest
from api_被封装测试接口.test_work_api import TestTpshopApiWork


# 创建测试函数继承unittest.TestCase
class TestTpshopWork(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 实例化封装的注册登录接口
        cls.zhuce_login_api = TestTpshopApiWork()
        # 实例化session
        cls.session = requests.Session()

    @classmethod
    def tearDownClass(cls):
        if cls.session != None:
            cls.session.close()

    # 注册成功
    def test_01_zhuce_success(self):
        #     发送获取验证码的接口请求
        self.zhuce_login_api.get_verify_zhuce(self.session)
        # 发送注册接口请求
        data_01 = {"auth_code": "TPSHOP", "scene": "1", "username": "13149201488",
                   "verify_code": "8888", "password": "519475228fe35ad067744465c42a19b2",
                   "password2": "519475228fe35ad067744465c42a19b2"}
        response_01 = self.zhuce_login_api.post_zhuce(data_01, self.session)
        #        断言注册结果
        self.assertEqual(200, response_01.status_code)
        self.assertEqual(1, response_01.json().get('status'))
        self.assertIn("注册成功", response_01.json().get("msg"))

    #     登录成功
    def test_02_login_success(self):
        #         发送获取验证码的接口请求
        self.zhuce_login_api.get_verify_login(self.session)
        #     发送登录接口请求
        data_02 = {"username": "13800138006", "password": "123456", "verify_code": "8888"}
        response_02 = self.zhuce_login_api.post_login(data_02, self.session)


#         断言登陆结果
        self.assertEqual(200, response_02.status_code)
        self.assertEqual(1, response_02.json().get('status'))
        self.assertIn("登陆成功", response_02.json().get("msg"))
