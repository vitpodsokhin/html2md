from flask import Flask, render_template, request
import html2markdown

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST' and 'html_string' in request.form:
        html_string = request.form['html_string']
        markdown_string = html2markdown.convert(html_string)
        return render_template('index.html', markdown_string=markdown_string)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
