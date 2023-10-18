from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    response_urls = []
    if request.method == 'POST':
        prompt = request.form.get('prompt').lower()

        # If-statement logic to generate URLs for the responses
        if prompt == "hello":
            response_urls = [url_for('hello_response_1'), url_for('hello_response_2'), url_for('hello_response_3')]
        elif prompt == "how are you?":
            response_urls = [url_for('how_are_you_response_1'), url_for('how_are_you_response_2'), url_for('how_are_you_response_3')]
        elif prompt == "what's your name?":
            response_urls = [url_for('name_response_1'), url_for('name_response_2'), url_for('name_response_3')]

    return render_template('index.html', response_urls=response_urls)

@app.route('/response/hello-1')
def hello_response_1():
    return render_template('hello_1.html')

@app.route('/response/hello-2')
def hello_response_2():
    return render_template('hello_2.html')

@app.route('/response/hello-3')
def hello_response_3():
    return render_template('hello_3.html')

@app.route('/response/how-are-you-1')
def how_are_you_response_1():
    return render_template('how_are_you_1.html')

@app.route('/response/how-are-you-2')
def how_are_you_response_2():
    return render_template('how_are_you_2.html')

@app.route('/response/how-are-you-3')
def how_are_you_response_3():
    return render_template('how_are_you_3.html')

@app.route('/response/name-1')
def name_response_1():
    return render_template('name_1.html')

@app.route('/response/name-2')
def name_response_2():
    return render_template('name_2.html')

@app.route('/response/name-3')
def name_response_3():
    return render_template('name_3.html')

if __name__ == '__main__':
    app.run(debug=True)
