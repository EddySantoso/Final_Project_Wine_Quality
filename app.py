from flask import Flask, render_template, request
from data import data_type
from prediction import prediction_data
## Initialize
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index_prediction():
    if request.method == 'POST':
        data = request.form
        data = data.to_dict()
        hasil = prediction_data(data)
        return render_template('result.html',hasil_prediction=hasil)
    return render_template('prediction.html',data_type=data_type)

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True,port=2929)