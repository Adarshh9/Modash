from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
from utils import get_req_data ,recommend_models ,extract_first_5_words
import requests

app = Flask(__name__)

# for deploying the application on web
url = "https://huggingface.co/datasets/adarshh9/vector-db-ModelMatch/resolve/main/vector_db.pickle?download=true"
destination = "data/vector_db.pickle"

response = requests.get(url, stream=True)
if response.status_code == 200:
    with open(destination, 'wb') as f:
        for chunk in response.iter_content(1024):
            if chunk:
                f.write(chunk)
        print(f"File downloaded successfully and saved to {destination}")
else:
    print(f"Failed to download file. Status code: {response.status_code}")

vectors ,df ,cv ,task_types ,tasks ,model_types ,frameworks = get_req_data()

@app.route('/')
def index():
    return render_template('index.html', types=task_types, tasks=tasks, model_types=model_types, frameworks=frameworks)

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    user_input = data['user_input']
    recommendations = recommend_models(cv ,df ,vectors ,user_input.lower())
    recommendations_list = []
    for index, row in recommendations.iterrows():
        model_tags = row['text']
        tags = extract_first_5_words(model_tags)
        recommendations_list.append({
            'modelId': row['modelId'],
            'downloads': row['downloads'],
            'likes': row['likes'],
            'createdAt': row['createdAt'],
            'author': row['author'],
            'tags': tags
        })
    return jsonify(recommendations_list)

if __name__ == '__main__':
    app.run()