import requests
from datetime import datetime
from io import BytesIO

# 假设你的 Django 服务运行在本地 8000 端口
url = 'http://127.0.0.1:8000/api/get_groups/'

# 登录接口为 /login/
login_url = 'http://127.0.0.1:8000/login/'
# 使用你的用户名和密码进行登录
# response = requests.post(login_url, data={'username': 'czxtest', 'password': 'czx20040718czx'})
# print(response.json())

response = requests.get(url)
print(response.json())

