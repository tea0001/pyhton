import re

x = input('请输入账号：')
r = re.match(r'\D([a-zA-Z0-9_]){5,15}', x)
print(r)
