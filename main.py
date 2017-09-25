from flask import Flask, request
from caesar import rotate_string
# Web Caesar Assignment Ann Kozminske  9/25/2017
app = Flask(__name__)
app.config['DEBUG'] = True

form = """
   <!DOCTYPE html>
    <html>
    <head>

    <style>
        form {{
        background-color: #eee;
        padding: 20px;

        margin: 0 auto;

        width: 540px;

        font: 16px sans-serif;

        border-radius: 10px;

        }}
        textarea {{

        margin: 10px 0;

        width: 540px;

        height: 120px;
        }}
    </style>

    </head>
    <body>
    <!-- Web-caesar form  -->
        <form action="/encrypt" method='POST'>
        <label for="rotate-by">Rotate by:
        <input id="rotate-by" type="text" name="rot" value="0" />
        </label>
        <label>Free Form Text Area
            <textarea name="text">{0}</textarea>
        </label>
        <input type="submit" value="Submit Query"/>
        </form>
    </body>

    </html>
"""


@app.route("/encrypt", methods=['POST'])   # route of the web app  
def encrypt():

    rot = request.form['rot']
    rot = int(rot) 
    text = request.form['text']
    encrypted_text=rotate_string(text, rot)
    
    return form.format(encrypted_text) #replaces {0} with encrypted_text string

@app.route("/") 
def index():   
    return form.format('') #replaces the {0} with empty string
    
app.run()