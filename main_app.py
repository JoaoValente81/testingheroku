from flask import Flask, render_template, request
from helper_function import run_model

app=Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def iris_pred():
    if request.method=='POST':
        sp_lenght=float(request.form['feature1'])
        pt_lenght=float(request.form['feature2'])
        pt_width=float(request.form['feature3'])
        sp_width=float(request.form['feature4'])

        list_features=[sp_lenght, pt_lenght, pt_width, sp_width]

        name=run_model(list_features)
        return render_template('main.html', pred=name)
    else:
        return render_template('main.html')

@app.route('/play', methods=['POST', 'GET'])
def video():
    return render_template('video.html')

if __name__=="__main__":
    app.run(debug=True,port=8732)

