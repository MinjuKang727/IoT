from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('share.html')

# 아래 코드는 반드시 맨 마지막에 있어야 함.
if __name__ == '__main__':
    app.run(host='192.168.30.204', port=5028)