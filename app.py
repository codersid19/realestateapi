from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load dataset
data = pd.read_csv('data/dataset_house_apartment.csv')

@app.route("/", methods=['GET'])
def welcome():
    return "Hellow WOrld"

@app.route('/properties', methods=['GET'])
def get_properties():
    location = request.args.get('location')
    if location:
        filtered = data[data['location'] == location]
    else:
        filtered = data
    return jsonify(filtered.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
