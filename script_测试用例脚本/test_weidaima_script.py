# 导包
import unittest, logging
from api_被封装测试接口.test_01_login_api import LoginApi
from api_被封装测试接口.test_weidaima_api import EmpoyeeApi
import app_配置信息

# 创建测试类
from utils_工具类 import assert_common


class TestIHRMEmployee(unittest.TestCase):
    # 初始化unittest的函数
    def setUp(self):
        #    实例化登录
        self.login_api = LoginApi()
        # 实例化员工
        self.emp_api = EmpoyeeApi()

    def tearDown(self):
        pass

    # 实现登录成功的接口
    def test01_login_success(self):
        # 发送登录的接口请求
        jsonData = {"mobile": "13800000002", "password": "123456"}
        response = self.login_api.login(jsonData,
                                        {"Content-Type": "application/json"})
        # 打印登录接口返回的结果
        logging.info("登录接口返回的结果为：{}".format(response.json()))
        # 提取登录返回的令牌
        token = 'Bearer ' + response.json().get('data')
        # 把令牌拼接成HEADERS并保存到全局变量HEADERS
        app_配置信息.HEADERS = {"Content-Type": "application/json", "Authorization": token}
        # 打印请求头
        logging.info("保存到全局变量中的请求头为：{}".format(app_配置信息.HEADERS))
        assert_common(self, 200, True, 10000, "操作成功",response)

    def test_02_add_emp(self):
        #         发送添加员工的接口请求
        response = self.emp_api.add_emp("鲤鱼王11", "138002003777", app_配置信息.HEADERS)
        #         打印添加员工的结果
        logging.info("添加结果:".format(response.json()))
        # 提取员工令牌保存到全局变量
        app_配置信息.EMP_ID = response.json().get("data").get("id")
        # 打印保存员工ID
        logging.info("保存的员工ID:{}".format(app_配置信息.EMP_ID))
        assert_common(self, 200, True, 10000, "操作成功", response)

    def test_03_query_emp(self):
        # 发送查询员工的接口请求
        response = self.emp_api.query_emp(app_配置信息.EMP_ID, app_配置信息.HEADERS)
        # 打印查询员工的数据
        logging.info("查询结果:{}".format(response.json()))
        assert_common(self, 200, True, 10000, "操作成功", response)

    def test_04_modify_emp(self):
        # 发送修改员工的接口请求
        response = self.emp_api.modify_emp(app_配置信息.EMP_ID, {"username": "暴鲤龙"}, app_配置信息.HEADERS)
        # 打印查询员工的数据
        logging.info("修改结果:{}".format(response.json()))
        assert_common(self, 200, True, 10000, "操作成功", response)

    def test_05_delete_emp(self):
        # 发送删除员工的接口请求
        response = self.emp_api.delete_emp(app_配置信息.EMP_ID, app_配置信息.HEADERS)
        # 打印查询员工的数据
        logging.info("删除结果:{}".format(response.json()))
        assert_common(self, 200, True, 10000, "操作成功", response)
