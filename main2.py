from flask import Flask, request, redirect#, render_template
import cgi
##import Jinja2, os
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
    </style>
</head>
<body> 

    <form action="fll" method="post">
        <input id="usrnme" type="text" name="usrnme"></input><br>{f}<br>
        <input id="psswd" type="text" name="psswd"></input><br>{s}<br>
        <input id="confm_psswd" type="text" name="confm_psswd"></input><br>{t}<br>
        <input id="eml" type="text" name="eml" /><br>{smd}<br>
        <input type="submit" />
    </form>
    
    
</body>
</html>
"""
def infowars():
    un = request.form['usrnme']
    pw = request.form['psswd']
    cpw = request.form['confm_psswd']
    emm = request.form['eml']
    wfrm = [un, pw, cpw, emm]
    return wfrm
def rrr():
    gg = ""
    if len(str(infowars[0])) >= 3:
        for j in (str(infowars[0])):
            if j == " ":
                break
                gg = gg + "U"
    else: 
        gg = gg + "U"
    if len(str(infowars[1])) >= 3:
        for u in (str(infowars[1])):
            if u == " ":
                break
                gg = gg + "P" 
        
        if (str(infowars[1])) != (str(infowars[2])):
            gg = gg + "C"
    else:
        gg = gg + "CP"
    if len(str(infowars[3])) > 0:
        if "@" not in (str(infowars[3])):
            gg = gg + "E"
    return gg

@app.route("/fll", methods=["POST"])
def frmfrm():
    rgb = int(len(str(rrr)))
    if rgb > 1:
        return redirect("/error")
    else:
        return redirect("/scss")
@app.route("/error")
def err():
    

    rgb = str(rrr)
    nam = ['','','','']
    if 'U' in rgb:
        nam[0] = "<p>This is not a valid username.</p>"

    if 'P' in rgb:
        nam[1] = "<p>This is not a valid password.</p>"
        
    if 'C' in rgb:
        nam[2] = "<p>These passwords do NOT match!</p>"
    if 'E' in rgb:
        nam[3] = "<p>That is not a valit email</p>" 
        
    return form.format(f = str(nam[0]), s = str(nam[1]), t = str(nam[2]), smd = str(nam[3]))


@app.route("/scss")
def scss():
    i = infowars
    return "<h1>Welcome," + str(i[0]) + "!</h1>"

@app.route("/")
def index():
    return form.format(f = "", s = "", t = "", smd = "")


app.run()