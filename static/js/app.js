// DOM Elements
const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const captureBtn = document.getElementById('captureBtn');
const emotionText = document.getElementById('emotionText');
const movieRecommendationsDiv = document.getElementById('movieRecommendations');
const loadingOverlay = document.getElementById('loadingOverlay');

// Initialize camera
async function initCamera() {
    try {
        const stream = await navigator.mediaDevices.getUserMedia({ video: true });
        video.srcObject = stream;
    } catch (err) {
        console.error('Error accessing camera:', err);
        alert('Unable to access camera. Please ensure you have granted camera permissions.');
    }
}

// Capture image and send to backend
function captureImage() {
    const context = canvas.getContext('2d');
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    context.drawImage(video, 0, 0, canvas.width, canvas.height);
    
    // Convert canvas to blob
    canvas.toBlob(async (blob) => {
        try {
            showLoading(true);
            const formData = new FormData();
            formData.append('image', blob, 'captured_image.jpg');
            
            // Send to backend
            const response = await fetch('/process_image', {
                method: 'POST',
                body: formData
            });
            
            if (!response.ok) throw new Error('Network response was not ok');
            
            const data = await response.json();
            updateUI(data);
        } catch (error) {
            console.error('Error:', error);
            alert('An error occurred. Please try again.');
        } finally {
            showLoading(false);
        }
    }, 'image/jpeg');
}

// Update UI with results
function updateUI(data) {
    // Update emotion
    emotionText.textContent = data.emotion.capitalize();
    
    // Update movie recommendations
    movieRecommendationsDiv.innerHTML = data.hollywood_movies.map(movie => `
        <div class="movie-card">
            <h3>${movie.title} (${movie.year})</h3>
        </div>
    `).join('');
     // Add Bollywood movies (using same card format for now)
     movieRecommendationsDiv.innerHTML += data.bollywood_movies.map(movie => `
        <div class="movie-card">
            <h3>${movie.title} (${movie.year})</h3>
        </div>
    `).join('');
}

// Show/hide loading overlay
function showLoading(show) {
    loadingOverlay.style.display = show ? 'flex' : 'none';
    captureBtn.disabled = show;
    captureBtn.textContent = show ? 'Processing...' : 'Capture Image';
}

// Event Listeners
captureBtn.addEventListener('click', captureImage);

// Initialize
initCamera(); 