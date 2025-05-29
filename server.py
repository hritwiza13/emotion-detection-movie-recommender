from flask import Flask, request, jsonify, send_from_directory
import os
import numpy as np
import cv2
from deepface import DeepFace

# Assume movie_recommender.py exists with get_movie_recommendations function
from movie_recommender import get_movie_recommendations

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def index():
    return send_from_directory(app.template_folder, 'index.html')

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

@app.route('/process_image', methods=['POST'])
def process_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400
    
    file = request.files['image']
    # Read image using OpenCV
    img_array = np.frombuffer(file.read(), np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    
    if img is None:
        return jsonify({'error': 'Invalid image format'}), 400
    
    try:
        # Detect emotion using DeepFace
        result = DeepFace.analyze(img, actions=['emotion'], enforce_detection=False)
        emotion = result[0]['dominant_emotion']
        
        # Get movie recommendations based on emotion (will implement later)
        hollywood_movies, bollywood_movies = get_movie_recommendations(emotion)
        
        # Placeholder response
        # hollywood_movies = [{'title': f'Hollywood Placeholder ({emotion})', 'year': ''}]
        # bollywood_movies = [{'title': f'Bollywood Placeholder ({emotion})', 'year': ''}]
        
        return jsonify({
            'emotion': emotion,
            'hollywood_movies': hollywood_movies,
            'bollywood_movies': bollywood_movies
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000) 