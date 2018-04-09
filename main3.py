from flask import Flask, request, render_template
import cgi
##import Jinja2, os
app = Flask(__name__)
app.config['DEBUG'] = True

form = render_template['index.html']
un = request.form['usrnme']
pw = request.form['psswd']
cpw = request.form['confm_psswd']
emm = request.form['eml']
wfrm = un + pw + cpw + emm

@app.route("/fll", methods=["POST"])
def frmfrm():
    if len(rrr) >= 1:
        return redirect("/error")
    else:
        return redirect("/scss")
@app.route("/error")
def err():
    


    nam = ""
    pss = ""
    cfp = ""
    eeml = "" 
    if 'U' in rrr:
        nam += "<p class='rj'>This is not a valid username.</p>"

    if "P" in rrr:
        pss += "<p class='rj'>This is not a valid password.</p>"
        
    if 'C' in rrr:
        cfp += "<p class='rj'>These passwords do NOT match!</p>"
    if "E" in rrr:
        eeml += "<p class='rj'>That is not a valit email</p>" 
        
    return form.format(nam, pss, cfp, eeml)
def rrr():
    if len(un) >= 3:
        for j in un:
            if j == " ":
                break
                gg += 'U'
    else: 
        gg += 'U'
    if len(pw) >= 3:
        for u in pw:
            if u == " ":
                break
                gg += 'P' 
        
        if pw != cpw:
            gg += 'C'
    else:
        gg += "CP"
    if len(emm) >= 1:
        if "@" not in emm:
            gg += "E"
    return gg

@app.route("/scss")
def scss():
    return "<h1>Welcome," + un + "!</h1>"

@app.route("/")
def index():
    return form.format("")


app.run()