from flask import Flask
from flask import render_template
from flask import request
from diaparser.parsers import Parser
from pathlib import Path
from spacy import displacy

parser = Parser.load('en_ewt-electra')

app = Flask(__name__)

# a route where we will display a welcome message via an HTML template
@app.route("/", methods=['POST','GET'])
def parse():
    if request.method == 'POST':  # this block is only entered when the form is submitted
        input = request.form.get("sentence")
        if input != None:
            parsed = parser.predict(input, text='en').sentences[0]
            print(parsed)
            image = displacy.render(parsed.to_displacy(), style='dep', manual=True, options={'compact': True, 'distance': 100})
            output_path = Path("static/css/img.svg")
            output_path.open("w", encoding="utf-8").write(image)
            return render_template('index.html', var=input)

    return render_template('index.html', var='Type here')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)

'''
 * Debugger is active!
 * Debugger PIN: 618-333-126
 * Running on all addresses.
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://192.168.1.2:8080/ (Press CTRL+C to quit)
 '''