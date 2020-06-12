# 实现员工管理登录
# 导包
import requests

# 发送ihrm登录的接口请求
response = requests.post(url="http://ihrm-test.itheima.net/api/sys/login",
                         json={"mobile": "13800000002", "password": "123456"},
                         headers={"Content-Type": "application/json"})
# 查看登录结果
print("登录结果:",response.json())