import process
from flask import Flask, request, render_template

# Khởi tạo flask app
app = Flask(__name__)

@app.route("/")
def home():
	return render_template('home.html')

# Khai báo các route cho API
@app.route("/predict", methods=["POST"])
def predict():
    s = request.form['textOrg']
    sumText = ""
    if s:
        sumText = process.solve(s)
    return render_template('home.html', original_text='{}'.format(s), prediction_text='Predict: {}'.format(sumText))

if __name__ == "__main__":
	print("App run!")
	app.run(debug=True)