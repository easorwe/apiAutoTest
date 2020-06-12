# 导包
import requests


# 定义封装的类
class TestTpshopApiWork:
    def __init__(self):
        # 验证码url和注册url以及登录url
        self.verify_zh = "http://localhost/index.php/Home/User/verify/type/user_reg.html"
        self.zhuce_url = "http://localhost/index.php/Home/User/reg.html"
        self.login_url = "http://localhost/index.php?m=Home&c=User&a=do_login"
        self.vetify_login = "http://localhost/index.php?m=Home&c=User&a=verify"

    # 获取注册验证码
    def get_verify_zhuce(self, session):
        return session.get(url=self.verify_zh)

    # 获取登录验证码
    def get_verify_login(self, session):
        return session.get(url=self.vetify_login)

    #     封装注册接口
    def post_zhuce(self, data_zhuce, session):
        response_zhuce = session.post(url=self.zhuce_url, data=data_zhuce)
        return response_zhuce

    # 封装登录接口
    def post_login(self, data_login, session):
        response_login = session.post(url=self.login_url, data=data_login)
        return response_login
