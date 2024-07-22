import os

import requests
from datetime import datetime
from io import BytesIO

# 假设你的 Django 服务运行在本地 8000 端口
url = 'http://127.0.0.1:8000/api/comparison/'

# 创建文件对象
# 遍历当前目录下的 test_codes 目录中的所有文件，用 open 打开文件并存储在文件列表中

files = []
for file in os.listdir('test_codes'):
    file_path = f'test_codes/{file}'
    files.append(('files', (file, open(file_path, 'rb'), 'application/octet-stream')))

data = {
    'comparison_type': 'group',
}

# 发送 POST 请求
response = requests.post(url, files=files, data=data)


# 打印响应内容
print(response.status_code)
print(response.json())
