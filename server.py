# ライブラリの取り込み
from flask import Flask, render_template
import urllib.request
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/my-link/<string:title>/<string:url>')
def my_link(title, url):
  dwonload(title, url)
  return 'DownLoad'


def dwonload(title, url):
	# URL,保存するパスを指定
	urls = "https://avatars1.githubusercontent.com/u/" + url ;
	save_name = title

	# ダウンロードする
	mem = urllib.request.urlopen(urls).read()
 
	# ファイルへの保存
	with open(save_name, mode="wb") as f:
		f.write(mem)

if __name__ == '__main__':
  app.run(debug=True)