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
@api.route('/items/<int:id>', methods=['GET'])
# データ比較
def check(id):
    db.connect()
    try:
        # 全件取得
        query = "SELECT * FROM sample_table"
        cur.execute(query)
        rows = cur.fetchall()
        # データのコミット
        cnx.commit()
    except Items.DoesNotExist:
        db.close()
        abort(404)
    
    flg = True
    if len(rows) > id:
        flg = True
    else:
        flg = False

    if flg == True:
        data = Items.select(Items.name).where(Items.id == id)
        data = "SELECT * FROM " + table_name + " WHERE id = %s"
        cur.execute(data, [id])
        rows = cur.fetchall()

        for row in rows:
            result = {
                "result": True,
                "rows":row,
            }
    else:
        result = {
            "result": flg,
            "result":flg,
        }
       
    db.close()
    return make_response(jsonify(result))


@api.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
        
if __name__ == '__main__':
    api.run(host='0.0.0.0',port=3000,debug=False) #host=0.0.0.0を指定することで外部からアクセス可能になる
