import os
import sys

# プロジェクトのルートディレクトリをPythonパスに追加
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# アプリケーションを実行
from my_memo_app.app import app

if __name__ == "__main__":
    app.run(debug=True) 