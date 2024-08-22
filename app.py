from flask import Flask, render_template, request, jsonify
import numpy as np
import sklearn
import pickle

app = Flask(__name__)

with open("./model/svm_model.pkl", 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def hello_world():
    return render_template('glasstypefinder.html')

@app.route('/find-glass', methods=['POST'])
def classify():
      x1 = request.form.get('ri')
      x2 = request.form.get('na')
      x3 = request.form.get('mg')
      x4 = request.form.get('al')
      x5 = request.form.get('si')
      x6 = request.form.get('k')
      x7 = request.form.get('ca')

      data = [int(x1), int(x2), int(x3), int(x4), int(x5), int(x6), int(x7)]

      X = np.array(data).reshape(1, -1)

      result = model.predict(X)

      glass_type = result[0].item()
      return jsonify({'glassType': glass_type})

if __name__ == '__main__':
       app.run()