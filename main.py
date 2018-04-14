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
            nam[0] = "This is not a valid username."

        if 'P' in rgb:
            nam[1] = "This is not a valid password."

        if 'C' in rgb:
            nam[2] = "These passwords do NOT match!"
        if 'E' in rgb:
            nam[3] = "That is not a valid email" 

        return render_template('home.html', f=str(nam[0]), s=str(nam[1]), t=str(nam[2]), sm=str(nam[3]), ufld=un, efld=emm)
        
        
        
        #return redirect("/error")
    else:
        return redirect("/scss?usrnme={u}".format(u = un))
    

@app.route("/scss")
def scss():
    usrnme = request.args.get('usrnme')
    return render_template('welcome.html', usrnme=str(usrnme))

@app.route("/")
def index():
   # template = jinja_env.get_template('index.html')
    usrnme = request.args.get('usrnme')
    email = request.args.get('eml')
    return render_template('home.html', f="", s="", t="", sm="", ufld="", efld="")


app.run()
