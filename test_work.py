# 导包
import requests


# # 获取注册验证码
# verify_zh = "http://localhost/index.php/Home/User/verify/type/user_reg.html"
# # # 实例化session
# session = requests.session()
# session.get(url=verify_zh)
#
# # 调用注册接口
# zhuce_url = "http://localhost/index.php/Home/User/reg.html"
# data = {"auth_code": "TPSHOP", "scene": "1", "username": "13145201418",
#         "verify_code": "8888", "password": "519475228fe35ad067744465c42a19b2",
#         "password2": "519475228fe35ad067744465c42a19b2"}
# response_zhuce = session.post(url=zhuce_url, data=data)
# # 查看结果
# print("注册结果为:", response_zhuce.json())
#
# # 获取登录验证码
# vetify_login = "http://localhost/index.php?m=Home&c=User&a=verify"
# session.get(url=vetify_login)
# # 发送登录接口请求
# login_url = "http://localhost/index.php?m=Home&c=User&a=do_login"
# data = {"username": "13800138006", "password": "123456", "verify_code": "8888"}
# response_login = session.post(url=login_url, data=data)
# # 查看结果
# print("登录结果为:", response_login.json())
# # 关闭连接
# session.close()


class pack_login_zhuce:
    def __init__(self):
        self.verify_zh = "http://localhost/index.php/Home/User/verify/type/user_reg.html"
        self.zhuce_url = "http://localhost/index.php/Home/User/reg.html"
        self.login_url = "http://localhost/index.php?m=Home&c=User&a=do_login"
        self.vetify_login = "http://localhost/index.php?m=Home&c=User&a=verify"

    def get_verify_zhuce(self, session):
        return session.get(url=self.verify_zh)

    def get_verify_login(self, session):
        return session.get(url=self.vetify_login)

    def post_zhuce(self, data_zhuce, session):
        response_zhuce = session.post(url=self.zhuce_url, data=data_zhuce)
        return response_zhuce

    def post_login(self, data_login, session):
        response_login = session.post(url=self.login_url, data=data_login)
        return response_login


session1 = requests.Session()
zhuce_login = pack_login_zhuce()
zhuce_login.get_verify_zhuce(session1)
data_zhuce = {"auth_code": "TPSHOP", "scene": "1", "username": "13145201477",
              "verify_code": "8888", "password": "519475228fe35ad067744465c42a19b2",
              "password2": "519475228fe35ad067744465c42a19b2"}
print("注册结果:", zhuce_login.post_zhuce(data_zhuce, session1).json())
zhuce_login.get_verify_login(session1)
data_login = {"username": "13800138006", "password": "123456", "verify_code": "8888"}
print("登录结果:",zhuce_login.post_login(data_login,session1).json())
