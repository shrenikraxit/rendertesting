document.addEventListener('DOMContentLoaded', () => {
    let video = document.getElementById('video');
    let canvas = document.getElementById('canvas');
    let context = canvas.getContext('2d');
    let preview = document.getElementById('preview');
    let cameraFrame = document.querySelector('.camera-frame');
    let timerElement = document.getElementById('timer');
    let captureButton = document.getElementById('capture');
    let retakeButton = document.getElementById('retake');
    let confirmButton = document.getElementById('confirm');
    let exportButton = document.getElementById('export-button');
    let translateButton = document.createElement('button');
    translateButton.id = 'translate-button';
    translateButton.textContent = 'Translate';
    translateButton.style.display = 'none';
    document.body.appendChild(translateButton);
    let modal = document.getElementById('modal');
    let modalImage = document.getElementById('modal-image');
    let closeModal = document.getElementById('close-modal');
    let images = [];
    let currentImageIndex = -1;
    let imageDataUrl = null
    let stream = null;
    const maxImages = 5;

    function startCamera() {
        navigator.mediaDevices.getUserMedia({ video: true })
            .then(mediaStream => {
                stream = mediaStream;
                video.srcObject = stream;
                video.onloadedmetadata = () => {
                    video.play();
                    canvas.width = video.videoWidth;
                    canvas.height = video.videoHeight;
                };
            })
    }

    function stopCamera() {
        if (stream) {
            let tracks = stream.getTracks();
            tracks.forEach(track => track.stop());
            stream = null;
        }
    }

    function startCountdown() {
        let countdown = 3;
        timerElement.style.display = 'block';

        let interval = setInterval(() => {
            if (countdown > 0) {
                timerElement.textContent = countdown;
            } else {
                clearInterval(interval);
                timerElement.style.display = 'none';
                captureImage();
            }
            countdown--;
        }, 1000);
    }

    function captureImage() {
        if (images.length < maxImages) {
            context.drawImage(video, 0, 0, canvas.width, canvas.height);
            imageDataUrl = canvas.toDataURL('image/jpeg');
            let img = document.createElement('img');
            img.src = imageDataUrl;
            img.className = 'preview-image';
            img.onclick = () => {
                modal.style.display = 'flex';
                modalImage.src = imageDataUrl;
            };

            if (currentImageIndex >= 0) {
                preview.replaceChild(img, preview.children[currentImageIndex]);
                images[currentImageIndex] = imageDataUrl;
            } else {
                images.push(imageDataUrl);
                preview.appendChild(img);
                currentImageIndex = images.length - 1;
            }

            captureButton.style.display = 'none'; // Hide capture button after image is captured
            retakeButton.style.display = 'inline';
            confirmButton.style.display = 'inline';
            exportButton.style.display = 'none';

            preview.classList.add('visible');
            stopCamera();
        } else {
            alert('Maximum of 5 images allowed.');
        }
    }

    function moveThumbnailsToScreen() {
        cameraFrame.style.display = 'none'; // Hide the camera frame
        preview.classList.add('spread-out'); // Spread out the thumbnails
        translateButton.style.display = 'block'; // Show the Translate button
        preview.classList.add('bigger-thumbnails'); // Make thumbnails bigger
    }

    // Event listeners
    captureButton.addEventListener('click', () => {
        startCountdown();
    });

    retakeButton.addEventListener('click', () => {
        preview.classList.remove('visible');
        captureButton.style.display = 'inline';
        retakeButton.style.display = 'none';
        confirmButton.style.display = 'none';
        modal.style.display = 'none';

        startCamera();
        setTimeout(startCountdown, 100); // Slight delay to ensure UI updates
    });

    confirmButton.addEventListener('click', () => {
        if (images.length === maxImages) {
            moveThumbnailsToScreen();
        } else {
            captureButton.style.display = 'inline'; // Show capture button for next image
            exportButton.style.display = 'inline';
            startCamera();
        }
        retakeButton.style.display = 'none';
        confirmButton.style.display = 'none';
        currentImageIndex = -1; // Reset index for the next picture
    });

    // JavaScript to upload images

    exportButton.addEventListener('click', () => {
      const formData = new FormData();
      formData.append('file', imageDataUrl);
      fetch('/upload', {
        method: 'POST',
        body: formData
      })
          //works up to this
      .then(response => response.json())
    });

    translateButton.addEventListener('click', () => {
        alert('Starting translation process...');
    });

    closeModal.addEventListener('click', () => {
        modal.style.display = 'none';
    });

    startCamera(); // Start the camera when the page loads
});
