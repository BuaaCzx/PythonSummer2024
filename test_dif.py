import difflib
from html import escape

# 定义两个字符串
text1 = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated."""

text2 = """Beautiful is better than ugly.
Explicit is better than implicit.
Readability counts.
Complex might be better than complicated."""

# 将字符串拆分为行列表
lines1 = text1.splitlines()
lines2 = text2.splitlines()

differ = difflib.Differ()

diff_result = differ.compare(lines1, lines2)

# 拼接成一个字符串，后附换行
diff_content = '\n'.join(diff_result)

# diff_content = ''.join(diff_result)
print(diff_content)

# 写入文件
# for line in diff_result:
#         print(line)

# d = difflib.Differ()
# diff = list(d.compare(text1.splitlines(keepends=True), text2.splitlines(keepends=True)))
# diff_content = ''.join(diff)
# with open('output2.dif', 'w') as f:
#     f.write(diff_content)

print("Diff file has been created.")