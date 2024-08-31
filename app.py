from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/upload', methods=['POST'])
def upload_file():
  if 'file' not in request.files:
    return 'No file part'

  file = request.files['file']
  file.save('uploaded_file.jpeg')  # Adjust the file name and path as needed

  return 'File uploaded successfully'

'''
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


'''






if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
