from flask import Flask, render_template
import led18

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/led/on')
def led_on() :
    # LED가 켜지는 코드
    led18.led18on()
    return 'LED ON'

@app.route('/led/off')
def led_off() :
    # LED가 지는 코드
    led18.led18off()
    return 'LED OFF'

# 아래 코드는 반드시 맨 마지막에 있어야 함.
if __name__ == '__main__':
    app.run(host='192.168.30.204', port=5028)