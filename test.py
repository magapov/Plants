from flask import Flask
from flask import render_template
import mraa
import time

app = Flask(__name__)

gpio0 = mraa.Gpio(40)
gpio1 = mraa.Gpio(38)
gpio2 = mraa.Gpio(37)

gpio0.write(0)
gpio1.write(0)
gpio2.write(0)

gpio0_state = 0
gpio1_state = 0
gpio2_state = 0

def rendTemplate():
    return render_template('index2.html',
        gpio0_status = (gpio0_state),
        gpio1_status = (gpio1_state),
        gpio2_status = (gpio2_state))

print("Init done")

@app.route('/')
def index():
    return rendTemplate()

@app.route('/A')
def led1on():
    gpio0.write(1)
    global gpio0_state
    gpio0_state = 1
    return rendTemplate()

@app.route('/a')
def led1off():
    gpio0.write(0)
    global gpio0_state
    gpio0_state = 0
    return rendTemplate()

@app.route('/B')
def led2on():
    gpio1.write(1)
    global gpio1_state
    gpio1_state = 1
    return rendTemplate()

@app.route('/b')
def led2off():
    gpio1.write(0)
    global gpio1_state
    gpio1_state = 0
    return rendTemplate()

@app.route('/C')
def led3on():
    gpio2.write(1)
    global gpio2_state
    gpio2_state = 1
    return rendTemplate()

@app.route('/c')
def led3off():
    gpio2.write(0)
    global gpio2_state
    gpio2_state = 0
    return rendTemplate()

if __name__=="__main__":
    print("Start")
    app.run(debug=True, host='192.168.0.4')
