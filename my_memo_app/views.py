from flask import render_template, redirect, url_for
from .app import app

# ==================================================
# ルーティング
# ==================================================
# モジュールのインポート
from werkzeug.exceptions import NotFound

# エラーハンドリング
@app.errorhandler(NotFound)
def show_404_page(error):
    msg = error.description
    print('エラー内容：',msg)
    return render_template('errors/404.html', msg=msg) , 404

@app.route('/')
def index():
    return redirect(url_for('auth.login'))
