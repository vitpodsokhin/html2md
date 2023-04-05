from flask import Flask, render_template, request
import html2markdown

app = Flask(__name__)
app.debug = True

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST' and 'htmlString' in request.form:
        html_string = request.form['htmlString']
        markdown_string = html2markdown.convert(html_string)
        return markdown_string
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
