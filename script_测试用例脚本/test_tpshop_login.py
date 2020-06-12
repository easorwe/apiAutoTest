# 导包
import requests
import unittest

# 创建测试函数继承unittest.TestCase
from api_被封装测试接口.tpshop_login_api import TestTpshopApi


class TestTpshopLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #     实例化封装的登录接口
        cls.login_api = TestTpshopApi()
        #         实例化session
        cls.session = requests.session()

    @classmethod
    def tearDownClass(cls):
        if cls.session != None:
            cls.session.close()
    # 登录成功
    def test_01_login_success(self):
        # 发送获取验证码的接口请求
        response = self.login_api.get_verify(self.session)
        # 断言验证码的返回数据
        self.assertIn("image", response.headers.get("Content-Type"))
        # 发送登录接口请求
        data = {"username": "13800138006", "password": "123456", "verify_code": "8888"}
        response = self.login_api.login(data, self.session)
        # 打印登录结果
        print("登录结果为:", response.json())
        # 断言登录
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, response.json().get("status"))
        self.assertIn("登陆成功", response.json().get("msg"))

# 账号不存在
    def test_02_login_none(self):
        # 发送获取验证码的接口请求
        response = self.login_api.get_verify(self.session)
        # 断言验证码的返回数据
        self.assertIn("image", response.headers.get("Content-Type"))
        # 发送登录接口请求
        data = {"username": "13800000009", "password": "123456", "verify_code": "8888"}
        response = self.login_api.login(data, self.session)
        # 打印登录结果
        print("登录结果为:", response.json())
        # 断言登录
        self.assertEqual(200, response.status_code)
        self.assertEqual(-1, response.json().get("status"))
        self.assertIn("账号不存在", response.json().get("msg"))

# 密码错误
    def test_03_login_error(self):
        # 发送获取验证码的接口请求
        response = self.login_api.get_verify(self.session)
        # 断言验证码的返回数据
        self.assertIn("image", response.headers.get("Content-Type"))
        # 发送登录接口请求
        data = {"username": "13800138006", "password": "error", "verify_code": "8888"}
        response = self.login_api.login(data, self.session)
        # 打印登录结果
        print("登录结果为:", response.json())
        # 断言登录
        self.assertEqual(200, response.status_code)
        self.assertEqual(-2, response.json().get("status"))
        self.assertIn("密码错误", response.json().get("msg"))
