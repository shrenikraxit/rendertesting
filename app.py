from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# In-memory storage for simplicity
stored_images = []

@app.route('/process-json', methods=['POST'])
def process_json():
    data = request.get_json()

    if not data or 'images' not in data:
        return jsonify({'error': 'No image data received'}), 400

    # Store the images
    global stored_images
    stored_images.extend(data['images'])

    return jsonify({'message': 'Images received successfully'}), 200

@app.route('/get-images', methods=['GET'])
def get_images():
    global stored_images
    return jsonify({'images': stored_images})

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
