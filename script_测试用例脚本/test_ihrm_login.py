import requests, logging, unittest
from api_被封装测试接口.test_01_login_api import LoginApi
import app_配置信息
# 创建unittest的类
from utils_工具类 import assert_common,read_login_data
from parameterized import parameterized


class TestIhrmLogin(unittest.TestCase):
    # 初始化
    def setUp(self):
        self.login_api = LoginApi()

    def tearDown(cls):
        pass

    filepath = app_配置信息.BASE_DIR + "/json_data/login_data_json.json"

    @parameterized.expand(read_login_data(filepath))
    def test01_login(self,case_name, request_body, success,code,message,http_code):
        # 使用封装的接口调用登录接口，并接收返回的响应数据
        response = self.login_api.login(request_body,
                                        {"Content-Type": "application/json"})
        # 打印响应数据
        logging.info("登录的结果为：{}".format(response.json()))
        assert_common(self, http_code, success, code, message, response)
    # 编写登陆成功按钮
    # def test_01_login_success(self, case_name,request_body,http_code, success, code, message):
    #     response = self.login_api.login(request_body,
    #                                     {"Content-Type": "application/json"})
    #     # 打印响应数据
    #     logging.info("登录结果为:{}".format(response.json()))
    #     # 断言
    #     assert_common(self, http_code, success, code, message, response)
        # self.assertEqual(200, response.status_code)
        # self.assertEqual(True, response.json().get("success"))
        # self.assertEqual(10000, response.json().get("code"))
        # self.assertIn("操作成功", response.json().get("message"))

    # def test_02_login_error(self):
    #     response = self.login_api.login({"mobile": "13800000002", "password": "error"},
    #                                     {"Content-Type": "application/json"})
    #     # 打印响应数据
    #     logging.info("登录结果为:{}".format(response.json()))
    #     # 断言
    #     assert_common(self, 200,False, 20001, "用户名或密码错误", response)
    #
    #
    # def test_03_login_not_excit(self):
    #     response = self.login_api.login({"mobile": "13800000009", "password": "123456"},
    #                                     {"Content-Type": "application/json"})
    #     # 打印响应数据
    #     logging.info("登录结果为:{}".format(response.json()))
    #     # 断言
    #     assert_common(self, 200, False, 20001, "用户名或密码错误", response)
    #
