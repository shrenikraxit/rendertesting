from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/process-json', methods=['POST'])
def process_json():
    data = request.get_json()

    if not data or 'images' not in data:
        return jsonify({'error': 'No image data received'}), 400

    # Process the images as needed (e.g., store them, analyze them)
    # Here we're just printing the received data
    print(f"Received {len(data['images'])} images")
    
    # Example: save JSON to a file
    with open('received_images.json', 'w') as f:
        json.dump(data, f, indent=4)
    
    return jsonify({'message': 'Images received successfully'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
