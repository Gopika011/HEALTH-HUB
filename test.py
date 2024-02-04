from flask import Flask, render_template, jsonify
import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('sample data5.csv')

# Sort the DataFrame based on the 'number of cases' column in descending order
sorted_df = df.sort_values(by='numberOfCases', ascending=False)

# Convert the DataFrame to JSON
json_data = sorted_df.to_json(orient='records')

app = Flask(__name__)

@app.route('/hospital')
def hello_world():
    return jsonify(json_data)  # Remove the extra dictionary

@app.route('/')
def hello():
    return render_template("hospital.html")

if __name__ == '__main__':
    app.run(debug=True)
