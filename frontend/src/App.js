import React, { useState, useRef, useEffect } from 'react';
import './App.css';

function App() {
  const [emotion, setEmotion] = useState(null);
  const [recommendations, setRecommendations] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const videoRef = useRef(null);
  const canvasRef = useRef(null);

  useEffect(() => {
    startCamera();
  }, []);

  const startCamera = async () => {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ video: true });
      if (videoRef.current) {
        videoRef.current.srcObject = stream;
      }
    } catch (err) {
      setError('Error accessing camera: ' + err.message);
    }
  };

  const captureAndSend = async () => {
    try {
      setLoading(true);
      setError(null);

      // Capture image from video
      const canvas = canvasRef.current;
      const video = videoRef.current;
      canvas.width = video.videoWidth;
      canvas.height = video.videoHeight;
      canvas.getContext('2d').drawImage(video, 0, 0);
      const imageData = canvas.toDataURL('image/jpeg');

      // Send to backend for emotion analysis
      const emotionResponse = await fetch('http://localhost:5000/api/analyze-emotion', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ image: imageData }),
      });

      if (!emotionResponse.ok) {
        throw new Error('Error analyzing emotion');
      }

      const { emotion: detectedEmotion } = await emotionResponse.json();
      setEmotion(detectedEmotion);

      // Get movie recommendations
      const recommendationsResponse = await fetch('http://localhost:5000/api/recommend-movies', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ emotion: detectedEmotion }),
      });

      if (!recommendationsResponse.ok) {
        throw new Error('Error getting recommendations');
      }

      const { recommendations: movieRecommendations } = await recommendationsResponse.json();
      setRecommendations(movieRecommendations);

    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Mood Movie Recommender 🎬</h1>
      </header>

      <main>
        <div className="camera-section">
          <video
            ref={videoRef}
            autoPlay
            playsInline
            className="camera-feed"
          />
          <canvas ref={canvasRef} style={{ display: 'none' }} />
          <button
            onClick={captureAndSend}
            disabled={loading}
            className="capture-button"
          >
            {loading ? 'Analyzing...' : 'Capture & Analyze'}
          </button>
        </div>

        {error && (
          <div className="error-message">
            {error}
          </div>
        )}

        {emotion && (
          <div className="emotion-section">
            <h2>Detected Emotion: {emotion}</h2>
          </div>
        )}

        {recommendations.length > 0 && (
          <div className="recommendations-section">
            <h2>Recommended Movies</h2>
            <div className="movie-grid">
              {recommendations.map((movie, index) => (
                <div key={index} className="movie-card">
                  {movie.poster_path && (
                    <img
                      src={movie.poster_path}
                      alt={movie.title}
                      className="movie-poster"
                    />
                  )}
                  <h3>{movie.title}</h3>
                  <p className="movie-year">{movie.release_date.split('-')[0]}</p>
                  <p className="movie-rating">Rating: {movie.vote_average}/10</p>
                  <p className="movie-overview">{movie.overview}</p>
                </div>
              ))}
            </div>
          </div>
        )}
      </main>
    </div>
  );
}

export default App;
