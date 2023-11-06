from flask import *

from chat import get_response
# from chat import get_response1
app = Flask(__name__)


@app.route("/")
def index_get():
    return render_template("base.html")
@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)
# print("would you like to hear some soothing songs, that is what i can do")

if __name__ == "__main__":
    app.run(debug=True)
