# 导包
import requests


# # 需求：tpshop登录
# verify_url = "http://localhost/index.php?m=Home&c=User&a=verify"
#
# # 实例化session
# session = requests.Session()
# session.get(url=verify_url)
#
# # 发送登录接口请求
# login_url = "http://localhost/index.php?m=Home&c=User&a=do_login"
# data = {"username": "13800138006", "password": "123456", "verify_code": "8888"}
# response_login = session.post(url=login_url, data=data)
# # 查看结果
# print("登录结果为:", response_login.json())
# # 关闭连接
# session.close()


class fengzhuangdemo:
    def __init__(self):
        self.verify_url = "http://localhost/index.php?m=Home&c=User&a=verify"
        self.login_url = "http://localhost/index.php?m=Home&c=User&a=do_login"

    def get_verify(self, session):
        print("get_verify里面的session的值", session)
        return session.get(url=self.verify_url)

    def login(self, data, session):
        print("login函数中的session的值:", session)
        response = session.post(url=self.login_url, data=data)
        return response


session2 = requests.Session()
fengzhaung = fengzhuangdemo()
print(fengzhaung.get_verify(session2).content)
data = {"username": "13800138006", "password": "123456", "verify_code": "8888"}
print(fengzhaung.login(data, session2).json())
