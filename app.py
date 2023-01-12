from flask import Flask, request
import os
import pytesseract

app= Flask(__name__)

def tesseract_it(path,save_path):
    # get image from path run tesseract on it and save the result in save_path as txt
    if os.path.exists(path):
        text = pytesseract.image_to_string(path)
        with open(save_path, 'w') as f:
            f.write(text)
            return True
    else:
        return False

@app.route('/')
def index():
    return 'Hello World'

@app.route('/upload', methods=['POST'])
def upload():
    files = request.files
    for file in files:
        temp_path= os.path.join('incoming-image', files[file].filename)
        files[file].save(temp_path)
        temp_save_path=os.path.join('outgoing-text', files[file].filename+'.txt')
        if tesseract_it(temp_path, temp_save_path):
            os.remove(temp_path)
            return 'success'
        else:
            return 'failed'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port= 3131, debug=True)
