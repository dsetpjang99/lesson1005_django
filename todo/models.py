from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# 建立todo資料表
class Todo(models.Model):
    # blank參數 =>內容是否可以為空(空代表可以不給予值)(預設為False)
    # auto_now_add參數 =>是否可以自動增加 (預設為False)
    title = models.CharField(max_length=255)
    text = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(blank=True, null=True)
    important = models.BooleanField(default=False)
    # 每一個todo資料，必須敘明是哪一位使用者新增的
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}--{self.title}"
