# coding: utf-8

from django.db import models


CHOICE = (('danger','high'),('warning','normal'),('primary','low'))

class Todomodel(models.Model):
    title = models.CharField(max_length=100) # 必ず引数を入れる。ChrFieldだと、最大文字数(max_length=~~~~)を入れないとエラーになる。
    memo = models.TextField()
    priority = models.CharField(
        max_length=50,
        choices = CHOICE # グローバルでCHOICEを定義しているが、そのままタプル型で記載してもOK（でも見やすくするため一般的には別で定義する。）
        )
    duedate = models.DateField()

    # オブジェクトが作成された際に、デフォルトで「aaa」を返しますよ。（aaaを別の名称にも変更できる。）
    def __str__(self):
        # return 'aaa'
        return self.title



