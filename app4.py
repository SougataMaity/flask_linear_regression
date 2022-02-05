from flask import Flask, render_template, request
app4 = Flask(__name__)

@app4.route('/')
def home():
    return render_template('index1.html')

@app4.route('/pred',methods = ['POST'])
def pred():
    v1 = request.form.get('v1')
    v2 = request.form.get('v2')
    return render_template('pred.html', prediction_value = 'Prediction price is {}'.format(v1))

if __name__ == '__main__':
    app4.run(debug=True)