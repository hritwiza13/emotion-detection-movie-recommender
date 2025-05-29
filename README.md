# Mood Movie Recommender 🎬

A web application that recommends movies based on your current mood, detected through facial expressions using your device's camera.

## Features

- Real-time facial emotion detection
- Camera integration for mood analysis
- Personalized movie recommendations based on detected emotions
- Modern and responsive user interface
- Secure API endpoints for emotion analysis and movie recommendations

## Tech Stack

- **Frontend**: React.js
- **Backend**: Python (Flask)
- **AI/ML**: TensorFlow.js for emotion detection
- **Movie Data**: TMDB API

## Prerequisites

- Python 3.8+
- Node.js 14+
- npm or yarn
- TMDB API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/mood_movie_recommender.git
cd mood_movie_recommender
```

2. Set up the backend:
```bash
# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
export TMDB_API_KEY=your_api_key_here  # On Windows: set TMDB_API_KEY=your_api_key_here
```

3. Set up the frontend:
```bash
cd frontend
npm install
```

## Running the Application

1. Start the backend server:
```bash
# From the root directory
python server.py
```

2. Start the frontend development server:
```bash
# From the frontend directory
npm start
```

3. Open your browser and visit `http://localhost:3000`

## Project Structure

```
mood_movie_recommender/
├── frontend/               # React frontend application
│   ├── src/               # Source files
│   ├── public/            # Static files
│   └── package.json       # Frontend dependencies
├── server.py              # Flask backend server
├── movie_recommender.py   # Movie recommendation logic
├── requirements.txt       # Python dependencies
└── README.md             # Project documentation
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [TMDB](https://www.themoviedb.org/) for movie data
- [TensorFlow.js](https://www.tensorflow.org/js) for emotion detection
- [React](https://reactjs.org/) for the frontend framework
- [Flask](https://flask.palletsprojects.com/) for the backend framework 