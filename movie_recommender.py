import os
import requests
import numpy as np
import tensorflow as tf
from PIL import Image
import io
import base64

class MovieRecommender:
    def __init__(self):
        self.tmdb_api_key = os.getenv('TMDB_API_KEY')
        self.tmdb_base_url = 'https://api.themoviedb.org/3'
        self.emotion_to_genre = {
            'happy': 35,  # Comedy
            'sad': 18,    # Drama
            'angry': 28,  # Action
            'surprise': 878,  # Science Fiction
            'fear': 27,   # Horror
            'disgust': 80,  # Crime
            'neutral': 10749  # Romance
        }
        
        # Load the emotion detection model
        self.model = tf.keras.models.load_model('emotion_model.h5')

    def analyze_emotion(self, image_data):
        """
        Analyze the emotion from the base64 encoded image
        """
        try:
            # Decode base64 image
            image_data = image_data.split(',')[1]
            image_bytes = base64.b64decode(image_data)
            image = Image.open(io.BytesIO(image_bytes))
            
            # Preprocess image
            image = image.resize((48, 48))
            image = np.array(image.convert('L'))
            image = image.reshape(1, 48, 48, 1)
            image = image / 255.0

            # Predict emotion
            emotions = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']
            prediction = self.model.predict(image)
            emotion = emotions[np.argmax(prediction)]

            return emotion

        except Exception as e:
            print(f"Error in emotion analysis: {str(e)}")
            return 'neutral'

    def get_recommendations(self, emotion):
        """
        Get movie recommendations based on the detected emotion
        """
        try:
            genre_id = self.emotion_to_genre.get(emotion, 35)  # Default to comedy if emotion not found
            
            # Get movies from TMDB API
            url = f"{self.tmdb_base_url}/discover/movie"
            params = {
                'api_key': self.tmdb_api_key,
                'with_genres': genre_id,
                'sort_by': 'popularity.desc',
                'page': 1
            }
            
            response = requests.get(url, params=params)
            response.raise_for_status()
            
            movies = response.json()['results'][:5]  # Get top 5 movies
            
            # Format movie data
            recommendations = []
            for movie in movies:
                recommendations.append({
                    'title': movie['title'],
                    'overview': movie['overview'],
                    'poster_path': f"https://image.tmdb.org/t/p/w500{movie['poster_path']}" if movie['poster_path'] else None,
                    'release_date': movie['release_date'],
                    'vote_average': movie['vote_average']
                })
            
            return recommendations

        except Exception as e:
            print(f"Error getting movie recommendations: {str(e)}")
            return [] 