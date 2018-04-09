from flask import Flask, request
import cgi
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
        <form action="csr" method="post">
           
            <input id="usrnme" type="text" name="usrnme"></input>
            <input id="psswd" type="text" name="psswd"></input>
            <input id="confm_psswd" type="text" name="confm_psswd"></input>
            <input id="eml" type="text" name="eml"></input>
            <input type="submit" />
        </form>
    </body>
</html>
"""
from caesar import rotate_character, encrypt


def un():
    message = request.form['usrnme']
    return message

def pw():
    rt = request.form['psswd']
    return rt
def cpw():
    crt= request.form['confm_psswd']
    return crt
def emm():
    ecm = request.form['eml']
    return ecm

@app.route("/csr", methods=['POST'])
def rme():
    
    
    return form.format(ecnrypmesse)

@app.route("/")
def index():
    return form.format('')
app.run()