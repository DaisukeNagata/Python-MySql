
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


# itemの詳細情報を取得
@api.route('/insert/<int:id>/<string:name>', methods=['GET'])
def getItem(id, name):
    print(id)
    print(name)
    db.connect()
    try:
        query = "INSERT INTO sample_table (id, name) VALUES (%s, %s)"
        
        # 単一行挿入
        cur.execute(query, (id, name))
        
        # データのコミット
        cnx.commit()
    except Items.DoesNotExist:
        db.close()
        abort(404)
    result = {
        "result": True,
    }
    db.close()
    return make_response(jsonify(result))

@api.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
        
if __name__ == '__main__':
    api.run(host='0.0.0.0',port=3000,debug=False) #host=0.0.0.0を指定することで外部からアクセス可能になる
