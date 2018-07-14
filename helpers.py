from flask import render_template

def apology(message="Sorry! Something went wrong..."):
    return render_template("apology.html", m=message)

def find_uname_from_id(d, user_id):
    for uname, data in d.items():
        if datap[1] == user_id:
            return uname
    return ""  
