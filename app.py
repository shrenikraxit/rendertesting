# Python (Flask)
from flask import Flask, request

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
  if 'file' not in request.files:
    return 'No file part'

  file = request.files['file']
  file.save('uploaded_file.jpeg')  # Adjust the file name and path as needed

  return 'File uploaded successfully'


if __name__ == "__main__":
    app.run(host=os.getenv('HOST'), port=int(os.getenv('PORT'),10000), debug=False)
