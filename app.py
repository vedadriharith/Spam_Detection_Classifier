from flask import Flask, render_template, request, jsonify
from utils import make_prediction
app=Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/predict", methods=["POST"])
def predict():
    email=request.form.get('email-content')
    prediction=make_prediction(email)
    return render_template("index.html",prediction=prediction, email=email)
@app.route("/api/predict",methods=["POST"])
def predict_api():
    data = request.get_json(force=True)
    email=data["email-content"]
    prediction=make_prediction(email)
    return jsonify({'prediction':prediction, 'email':email})
if __name__=="__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)