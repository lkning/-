import hashlib
from django.db import models

class UserInfo(models.Model):
    username = models.CharField("用户名", max_length=64, unique=True)
    password = models.CharField("密码", max_length=64)
    uid = models.CharField(verbose_name='个人唯一ID',max_length=64, unique=True)

    wx_id = models.CharField(verbose_name="微信ID", max_length=128, blank=True, null=True, db_index=True)

    def save(self, *args, **kwargs):
        # 创建用户时，为用户自动生成个人唯一ID
        if not self.pk:
            m = hashlib.md5()
            m.update(self.username.encode(encoding="utf-8"))
            self.uid = m.hexdigest()
        super(UserInfo, self).save(*args, **kwargs)

# UserInfo.objects.create(username='宋涛',password='123')
#
# obj = UserInfo(username='宋涛',password='123')
# obj.save()

# obj = UserInfo.objects.get(id=1)
# obj.username = "asdfasd"
# obj.save()