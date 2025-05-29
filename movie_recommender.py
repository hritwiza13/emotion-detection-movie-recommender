def get_movie_recommendations(emotion):
    """
    Provides placeholder movie recommendations based on emotion.
    In a real application, this would involve a more sophisticated recommendation logic.
    """
    emotion_lower = emotion.lower()

    # Simple mapping of emotions to placeholder movie lists
    if emotion_lower == 'happy':
        hollywood = [{'title': 'Happy Hollywood Movie 1', 'year': ''}, {'title': 'Happy Hollywood Movie 2', 'year': ''}]
        bollywood = [{'title': 'Happy Bollywood Movie 1', 'year': ''}, {'title': 'Happy Bollywood Movie 2', 'year': ''}]
    elif emotion_lower == 'sad':
        hollywood = [{'title': 'Sad Hollywood Movie 1', 'year': ''}, {'title': 'Sad Hollywood Movie 2', 'year': ''}]
        bollywood = [{'title': 'Sad Bollywood Movie 1', 'year': ''}, {'title': 'Sad Bollywood Movie 2', 'year': ''}]
    elif emotion_lower == 'angry':
        hollywood = [{'title': 'Angry Hollywood Movie 1', 'year': ''}, {'title': 'Angry Hollywood Movie 2', 'year': ''}]
        bollywood = [{'title': 'Angry Bollywood Movie 1', 'year': ''}, {'title': 'Angry Bollywood Movie 2', 'year': ''}]
    # Add more emotions as needed
    else:
        # Default recommendations for other emotions or if emotion detection fails
        hollywood = [{'title': 'Neutral Hollywood Movie 1', 'year': ''}, {'title': 'Neutral Hollywood Movie 2', 'year': ''}]
        bollywood = [{'title': 'Neutral Bollywood Movie 1', 'year': ''}, {'title': 'Neutral Bollywood Movie 2', 'year': ''}]

    return hollywood, bollywood 