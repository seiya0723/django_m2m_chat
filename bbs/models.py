from django.db import models
from django.conf import settings

from django.utils import timezone




class Topic(models.Model):

    comment     = models.CharField(verbose_name="コメント",max_length=2000)
    user        = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name="投稿者",on_delete=models.CASCADE)

    def __str__(self):
        return self.comment


class ChatGroup(models.Model):

    dt          = models.DateTimeField(verbose_name="グループ作成日",default=timezone.now)

    #TODO:もしこれがLINEを模したWEBアプリであればグループ名を設定できるようにする
    #name        = models.CharField(verbose_name="グループ名", max_length=50)

    member      = models.ManyToManyField(settings.AUTH_USER_MODEL,verbose_name="グループ内メンバー")

    def chats(self):
        return Chat.objects.filter(group=self.id).order_by("dt")


class Chat(models.Model):

    dt          = models.DateTimeField(verbose_name="グループ作成日",default=timezone.now)
    group       = models.ForeignKey(ChatGroup, verbose_name="所属チャットグループ", on_delete=models.CASCADE)

    message     = models.CharField(verbose_name="メッセージ",max_length=20000)
    user        = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name="投稿者",on_delete=models.CASCADE)

