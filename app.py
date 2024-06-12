from flask import Flask, render_template
from flask_flatpages import FlatPages

app = Flask(__name__)
app.config['FLATPAGES_EXTENSION'] = '.md'
pages = FlatPages(app)

@app.route('/')
def index():
    return render_template('index.html', pages=pages)

@app.route('/<path:path>/')
def page(path):
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)

if __name__ == '__main__':
    app.run(debug=True)

