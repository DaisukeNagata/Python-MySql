import mysql.connector

# 接続
config = {
    'user': 'root',
    'password': '',
    'host': '127.0.0.1',
    'database': 'mysql'
}
cnx = mysql.connector.connect(**config)
cur = cnx.cursor()

# 接続できているかどうか確認
print(cnx.is_connected())

# 指定のデータを削除
def deleate():
    # SQLクエリ実行（データ削除）
    sql = 'DELETE FROM sample_table WHERE name = "Test"'
    cur.execute(sql)

# テーブル作成
def create_table():
    query = """CREATE TABLE IF NOT EXISTS sample_table (
        id int NOT NULL,
        name VARCHAR(20) NOT NULL
        )"""
    cur.execute(query)
    
# データ挿入
def insert():
    try:
        query = "INSERT INTO sample_table (id, name) VALUES (%s, %s)"
 
        # 単一行挿入
        cur.execute(query, (1, "hoge"))
 
        # タプルで複数行挿入
      #  dataset_tpl = [
      #      (2, "fuga"),
      #      (3, "piyo"),
      #      (4, "hogefuga"),
      #      (5, "fugafuga")
      #   ]
 
        # リストでもいける
        dataset_list = [
            [2, "fuga"],
            [3, "piyo"],
            [4, "hogefuga"],
            [5, "fugafuga"],
            [6, "Test"]
        ]
 
        cur.executemany(query, dataset_list)
 
        # データのコミット
        cnx.commit()
 
    except Exception as e:
        # エラー時にロールバック
        cnx.rollback()
        raise e
        
# データ取得
def select():
    # 全件取得
    query = "SELECT * FROM sample_table"
    cur.execute(query)
 
    print("all:")
    rows = cur.fetchall()
    print(rows)
        #for row in rows:
        #print(row)
 
    # テーブル名を変数で入れる場合は文字列でつなぐ
    table_name = "sample_table"
 
    # プリペアードステートメントで絞り込み
    query = "SELECT * FROM " + table_name + " WHERE name = %s"
    cur.execute(query, ["fugafuga"])
 
    print("fugafuga:")
    rows = cur.fetchall()
    for row in rows:
        print(row)
# データ比較
class checkData():
    def __init__(self, n):
        self.a = n
    
    def check(self):
        print(self.a)

        # 全件取得
        query = "SELECT * FROM sample_table"
        cur.execute(query)
        rows = cur.fetchall()
        
        if len(rows) > self.a:
            print("false")
        else:
            print("true")
#create_table()
#c=checkData(4)
#c.check()
insert()
#deleate()
#select()
