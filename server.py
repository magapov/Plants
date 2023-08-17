from flask import Flask
from flask import render_template
import mraa
import time

app = Flask(__name__)

nEn = mraa.Gpio(7)
s0  = mraa.Gpio(40)
s1  = mraa.Gpio(38)
s2  = mraa.Gpio(37)
s3  = mraa.Gpio(36)
sig = mraa.Gpio(35)

nEn.dir(mraa.DIR_OUT)
s0.dir(mraa.DIR_OUT)
s1.dir(mraa.DIR_OUT)
s2.dir(mraa.DIR_OUT)
s3.dir(mraa.DIR_OUT)
sig.dir(mraa.DIR_OUT)

nEn.write(1)
s0.write(0)
s1.write(0)
s2.write(0)
s3.write(0)
sig.write(0)

nEn_state = 1
s0_state = 0
s1_state = 0
s2_state = 0
s3_state = 0
sig_state = 0

ch_active = -1

print("Init done")

def setActive(ch=-1):
    global nEn_active
    global s0_state
    global s1_state
    global s2_state
    global s3_state
    global ch_active

    if ch == -1:
        if (ch_active != -1):
            nEn_state = 1
            nEn.write(nEn_state)
            s0_state = ch_active & 0x01
            s1_state = (ch_active & 0x02) >> 1
            s2_state = (ch_active & 0x04) >> 2
            s3_state = (ch_active & 0x08) >> 3
            print ("s0: ", s0_state)
            print ("s1: ", s1_state)
            print ("s2: ", s2_state)
            print ("s3: ", s3_state)
            print ("sig: 0")
            s0.write(s0_state)
            s1.write(s1_state)
            s2.write(s2_state)
            s3.write(s3_state)
            sig.write(0)
            nEn_state = 0
            nEn.write(nEn_state)
            ch_active = -1
    else:
        nEn_state = 1
        nEn.write(nEn_state)
        s0_state = ch & 0x01
        s1_state = (ch & 0x02) >> 1
        s2_state = (ch & 0x04) >> 2
        s3_state = (ch & 0x08) >> 3
        print ("s0: ", s0_state)
        print ("s1: ", s1_state)
        print ("s2: ", s2_state)
        print ("s3: ", s3_state)
        print ("sig: 1")
        s0.write(s0_state)
        s1.write(s1_state)
        s2.write(s2_state)
        s3.write(s3_state)
        sig.write(1)
        nEn_state = 0
        nEn.write(nEn_state)
        ch_active = ch

def rendTemplate():
    global ch_active
    return render_template('index.html',
        ch0_status = int(ch_active == 0),
        ch1_status = int(ch_active == 1),
        ch2_status = int(ch_active == 2),
        ch3_status = int(ch_active == 3),
        ch4_status = int(ch_active == 4),
        ch5_status = int(ch_active == 5),
        ch6_status = int(ch_active == 6),
        ch7_status = int(ch_active == 7),
        ch8_status = int(ch_active == 8),
        ch9_status = int(ch_active == 9),
        ch10_status = int(ch_active == 10),
        ch11_status = int(ch_active == 11),
        ch12_status = int(ch_active == 12),
        ch13_status = int(ch_active == 13),
        ch14_status = int(ch_active == 14),
        ch15_status = int(ch_active == 15))

@app.route('/')
@app.route('/off')
def off():
    setActive(-1)
    return rendTemplate()

@app.route('/ch0')
def ch0on():
    setActive(0)
    return rendTemplate()

@app.route('/ch1')
def ch1on():
    setActive(1)
    return rendTemplate()

@app.route('/ch2')
def ch2on():
    setActive(2)
    return rendTemplate()

@app.route('/ch3')
def ch3on():
    setActive(3)
    return rendTemplate()

@app.route('/ch4')
def ch4on():
    setActive(4)
    return rendTemplate()

@app.route('/ch5')
def ch5on():
    setActive(5)
    return rendTemplate()

@app.route('/ch6')
def ch6on():
    setActive(6)
    return rendTemplate()

@app.route('/ch7')
def ch7on():
    setActive(7)
    return rendTemplate()

@app.route('/ch8')
def ch8on():
    setActive(8)
    return rendTemplate()

@app.route('/ch9')
def ch9on():
    setActive(9)
    return rendTemplate()

@app.route('/ch10')
def ch10on():
    setActive(10)
    return rendTemplate()

@app.route('/ch11')
def ch11on():
    setActive(11)
    return rendTemplate()

@app.route('/ch12')
def ch12on():
    setActive(12)
    return rendTemplate()

@app.route('/ch13')
def ch13on():
    setActive(13)
    return rendTemplate()

@app.route('/ch14')
def ch14on():
    setActive(14)
    return rendTemplate()

@app.route('/ch15')
def ch15on():
    setActive(15)
    return rendTemplate()

if __name__=="__main__":
    print("Start")
    app.run(debug=True, host='192.168.0.4')

