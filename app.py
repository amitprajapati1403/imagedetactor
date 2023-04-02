from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['get', 'post'])
def index():
    if request.method == 'post':
        file = request.files['image']
        file.save(file.filename)
        return 'Image uploaded!'
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run()
