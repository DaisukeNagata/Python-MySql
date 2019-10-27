# -*- coding: utf-8 -*-
import peewee

# データベースを指定
db = peewee.SqliteDatabase("mysql.db")

# ユーザーモデルを定義
class User(peewee.Model):
    userId = peewee.TextField()
    userCompany = peewee.TextField()
    userDiscountRate = peewee.IntegerField()

    class Meta:
        database = db

# ユーザーテーブル作成
User.create_table()
