from flask import Flask, request, redirect, render_template
import cgi
app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/fll", methods=["POST"])
def frmfrm():
    un = request.form['usrnme']
    pw = request.form['psswd']
    cpw = request.form['confm_psswd']
    emm = request.form['eml']
    gg = ""
    if len(un) >= 3 and len(un) <= 20:
        for j in un:
            if j == " ":
                gg = gg + "U"
    else: 
        gg = gg + "U"
    if len(pw) >= 3 and len(pw) <= 20:
        for u in pw:
            if u == " ":
                break
                gg = gg + "P" 
        
        if pw != cpw:
            gg = gg + "C"
    else:
        gg = gg + "CP"
    if len(emm) > 0:
        if "@" in emm and "." in emm and len(emm) >= 3 and len(emm) <= 20:
            gg = gg
        else: #"@" not in emm:
            gg = gg + "E"
   
    
    if len(gg) > 0:
        rgb = str(gg)
        nam = ['','','','']
        if 'U' in rgb:
            nam[0] = "<p>This is not a valid username.</p>"

        if 'P' in rgb:
            nam[1] = "<p>This is not a valid password.</p>"

        if 'C' in rgb:
            nam[2] = "<p>These passwords do NOT match!</p>"
        if 'E' in rgb:
            nam[3] = "<p>That is not a valid email</p>" 

        return render_template('index.html', f=str(nam[0]), s=str(nam[1]), t=str(nam[2]), sm=str(nam[3]), ufld=usr, efld=email)
        
        
        
        #return redirect("/error")
    else:
        return redirect("/scss?usrnme={0}".format(un))
    

@app.route("/scss")
def scss():
    usrnme = request.args.get('usrnme')
    return render_template('welcome.html', usrnme=usrnme)

@app.route("/")
def index():
   # template = jinja_env.get_template('index.html')
    usrnme = request.args.get('usrnme')
    email = request.args.get('eml')
    return render_template('index.html', f="", s="", t="", sm="", ufld="", efld="")


app.run()
