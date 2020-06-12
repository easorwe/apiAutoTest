# 导入request
import requests

# 发送的登录的接口请求
response = requests.post(url="http://ihrm-test.itheima.net/api/sys/login",
                         json={"mobile": "13800000002", "password": "123456"},
                         headers={"Content-Type": "application/json"}
                         )
# 打印登陆结果
print("登陆结果为:",response.json())
# 提取登录返回的令牌
token = "Bearer " + response.json().get("data")
print("登陆令牌:",token)

# 发送员工登录接口
headers =  {"Content-Type": "application/json", "Authorization": token}
# 添加需要的请求头
response =requests.post(url="http://ihrm-test.itheima.net" + "/api/sys/user",
                        json={
                            "username": "奥观海97787",
                            "mobile": "1593362528",
                            "timeOfEntry": "2020-05-05",
                            "formOfEmployment": 1,
                            "departmentName": "测试部",
                            "departmentId": "1063678149528784896",
                            "correctionTime": "2020-05-30T16:00:00.000Z"
                        },
                        headers=headers)
# 打印添加员工的接口
print("添加员工的接口返回数据:",response.json())
# 提取员工的id
emp_id = response.json().get("data").get("id")
print("员工id:",emp_id)

# 拼接查询员工接口的url
query_url = "http://ihrm-test.itheima.net"+"/api/sys/user"+"/"+emp_id
print("查询员工接口url:",query_url)
# 发送查询员工接口请求
response = requests.get(url=query_url,headers=headers)
# 打印查询员工的结果
print("查询结果:",response.json())

# 修改员工的url
modify_url  = "http://ihrm-test.itheima.net"+"/api/sys/user"+"/"+emp_id
# 发送修改员工的接口请求
response = requests.put(url=modify_url,json={"username":"爱泼斯坦"},headers=headers)
# 打印修改员工的结果
print("修改结果:",response.json())

#删除员工的url
delete_url ="http://ihrm-test.itheima.net"+"/api/sys/user"+"/"+emp_id
## 发送删除员工的接口请求
response = requests.delete(url=delete_url,headers=headers)
# 打印删除结果
print("删除员工结果:",response.json())












