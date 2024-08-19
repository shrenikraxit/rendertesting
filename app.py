from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/export-images', methods=['POST'])
def export_images():
    data = request.get_json()
    images = data.get('images', [])

    if images:
        # Here, you can save the images or process them as needed
        # For example, save them to the filesystem or a database

        return jsonify({"message": "Images received and processed successfully!"}), 200
    else:
        return jsonify({"message": "No images received!"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
