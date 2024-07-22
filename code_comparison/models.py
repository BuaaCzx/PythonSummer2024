from django.db import models
from django.contrib.auth.models import User


class CodeComparisonHistory(models.Model):
    # 历史记录表，目前是一对一比较的记录
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file1 = models.TextField()  # 代码内容
    file2 = models.TextField()
    file1_name = models.CharField(max_length=255)  # 文件名
    file2_name = models.CharField(max_length=255)
    similarity_ratio = models.FloatField()
    diff_content = models.TextField()  # 差异内容
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.file1_name} vs {self.file2_name} = {self.similarity_ratio}"
