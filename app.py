from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='templates', static_folder='static')

# Mapping file names to specific images
file_image_mapping = {
    '1': 'https://bubobirding.com/wp-content/uploads/2019/11/Yellow-throated-Bulbul_20191027_1110503.jpg',
    '2': 'https://bubobirding.com/wp-content/uploads/2019/11/Malabar-Lark_20151228_0043.jpg',
    '3': 'https://bubobirding.com/wp-content/uploads/2019/11/Nilgiri-Flycatcher_20171021_1080469.jpg',  
    '4': 'https://bubobirding.com/wp-content/uploads/2020/01/White-bellied-Sholakili_20200110_1120569.jpg',
    '5': 'https://bubobirding.com/wp-content/uploads/2019/11/Blue-winged-Parakeet_200909239782G.jpg'
}

@app.route('/')
def index():
    return render_template('index.html', outputs=None)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'audioFile' not in request.files:
        return 'No file part'
    file = request.files['audioFile']
    if file.filename == '':
        return 'No selected file'

    file.save(file.filename)

    # Determine the image based on the file name
    image_url = None
    for key in file_image_mapping:
        if key in file.filename:
            image_url = file_image_mapping[key]
            break

    if not image_url:
        return 'File name does not match any predefined patterns'

    outputs = {
        'image_path': image_url
    }

    return redirect(url_for('upload_success', image_url=image_url))

@app.route('/success')
def upload_success():
    image_url = request.args.get('image_url')
    outputs = {
        'image_path': image_url
    }
    return render_template('index.html', outputs=outputs, scroll_to_section=3)

if __name__ == '__main__':
    app.run(debug=True)


