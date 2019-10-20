from flask import Flask, jsonify, abort, make_response
import peewee as pe
import mysql.connector
db = pe.MySQLDatabase('mysql', user='root', password='',host='127.0.0.1')
# 接続
config = {
    'user': 'root',
    'password': '',
    'host': '127.0.0.1',
    'database': 'mysql'
}
cnx = mysql.connector.connect(**config)
cur = cnx.cursor()

class UnknownField(object):
    def __init__(self, *_, **__): pass

# モデル共通
class BaseModel(pe.Model):
    class Meta:
        database = db

# データテーブルのモデル
class Items(BaseModel):
    id = pe.IntegerField()
    name = pe.CharField()
    class Meta:
        db_table = 'sample_table' # テーブル名を指定

api = Flask(__name__)
api.config['JSON_AS_ASCII'] = False

# itemの詳細情報を取得
@api.route('/delete', methods=['GET'])
# 指定のデータを削除
def delete():
    sql = 'DELETE FROM sample_table'
    cur.execute(sql)

    # データのコミット
    cnx.commit()
    cur.close()
    cnx.close()
    return make_response()

@api.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
        
if __name__ == '__main__':
    api.run(host='0.0.0.0',port=3000,debug=False) #host=0.0.0.0を指定することで外部からアクセス可能になる
