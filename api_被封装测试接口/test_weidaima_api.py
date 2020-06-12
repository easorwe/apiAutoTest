import requests


class EmpoyeeApi:
    def __init__(self):
        self.emp_url = "http://ihrm-test.itheima.net" + "/api/sys/user"

    def add_emp(self, username, mobile, headers, ):
        jsonData = {
            "username": username,
            "mobile": mobile,
            "timeOfEntry": "2020-05-05",
            "formOfEmployment": 1,
            "departmentName": "测试部",
            "departmentId": "1063678149528784896",
            "correctionTime": "2020-05-30T16:00:00.000Z"
        }
        return requests.post(url=self.emp_url, json=jsonData, headers=headers)

    def query_emp(self, emp_id, headers):
        # 拼接查询员工的url
        query_url = self.emp_url + "/" + emp_id
        # 发送查询员工的接口请求.并return返回结果
        return requests.get(url=query_url, headers=headers)

    def modify_emp(self, emp_id, jsonData, headers):
        # 拼接查询员工的url
        modify_url = self.emp_url + "/" + emp_id
        # 发送查询员工的接口请求.并return返回结果
        return requests.put(url=modify_url, json=jsonData, headers=headers)

    def delete_emp(self, emp_id, headers):
        # 拼接查询员工的urld
        delete_url = self.emp_url + "/" + emp_id
        # 发送查询员工的接口请求.并return返回结果
        return requests.get(url=delete_url, headers=headers)
