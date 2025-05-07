import os
import sys

# プロジェクトのルートディレクトリをPythonパスに追加
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

# アプリケーションを実行
from my_memo_app.app import app

if __name__ == '__main__':
    app.run(debug=True) 