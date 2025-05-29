from flask import Flask, request, jsonify
import os
import numpy as np
import cv2
from deepface import DeepFace
import logging
from logging.handlers import RotatingFileHandler
from flask_cors import CORS
from dotenv import load_dotenv
import requests
import json
from movie_recommender import MovieRecommender

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Configure logging
if not os.path.exists('logs'):
    os.makedirs('logs')
file_handler = RotatingFileHandler('logs/app.log', maxBytes=10240, backupCount=10)
file_handler.setFormatter(logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
))
file_handler.setLevel(logging.INFO)
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)
app.logger.info('Mood Movie Recommender startup')

# Initialize movie recommender
movie_recommender = MovieRecommender()

@app.route('/api/analyze-emotion', methods=['POST'])
def analyze_emotion():
    try:
        # Get the image data from the request
        image_data = request.json.get('image')
        if not image_data:
            return jsonify({'error': 'No image data provided'}), 400

        # Analyze emotion using the movie recommender
        emotion = movie_recommender.analyze_emotion(image_data)
        return jsonify({'emotion': emotion})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/recommend-movies', methods=['POST'])
def recommend_movies():
    try:
        # Get the emotion from the request
        emotion = request.json.get('emotion')
        if not emotion:
            return jsonify({'error': 'No emotion provided'}), 400

        # Get movie recommendations
        recommendations = movie_recommender.get_recommendations(emotion)
        return jsonify({'recommendations': recommendations})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'})

@app.errorhandler(404)
def not_found_error(error):
    app.logger.error(f'Page not found: {request.url}')
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    app.logger.error(f'Server Error: {error}')
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True) 