from helpers import apology
from models import *
import requests, json
import datetime

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/", methods=["GET", "POST"])
def index():
    # redirecting to login form
    if request.method == "GET":
        return redirect(url_for("login"))
    # welcome user if successful login
    if request.method == "POST":
        uname = db.query(UserLogin).get(session["user_id"])
        return render_template("index.html", name=uname)

@app.route("/login", methods=["GET", "POST"])
def login():
    # forget current user_id if any
    db.remove()

    # allow login
    if request.method == "GET":
        return render_template("login.html")

    # process login
    elif request.method == "POST":
        # collect username and password from login form
        uname = request.form.get("username")
        pw = request.form.get("password")

        # check validity of username and password
        if not uname:
            return apology("must provide username")
        elif not pw:
            return apology("must provide password")

        try:
            pw_dbSQLA = db.query(UserLogin.password).filter(UserLogin.name.in_([uname])).first()[0]
            #dbSQLA.users[uname][0]
        except TypeError:
            return apology("username does not exist")
        if pw_dbSQLA != pw:
            return apology("password incorrect")

        # Login user on success, redirect to index page
        else:
            session["user_id"] = db.query(UserLogin.id).filter(UserLogin.name.in_([uname])).first()[0]
            #return render_template("hello.html", name=uname)
            return redirect(url_for("hello", name=uname))

@app.route("/hello", methods=["GET"])
def hello():
    uname = request.args['name']
    return render_template("hello.html", name=uname)

@app.route("/search", methods=["POST"])
def search():
    #search = request.args['search']
    search = request.form.get("search")
    search_by_zipcode = search.isdigit()

    # if looking by zipcode
    if search_by_zipcode:
        answer = db.query(ZIPS).filter(cast(ZIPS.zipcode, sqlalchemy.String).contains(search)).all()

    else:
        answer = db.query(ZIPS).filter(ZIPS.city.contains(search)).all()
    return render_template("ziplist.html", search=search, data=answer)

@app.route("/zip")
def zip():
    id = request.args.get('id')
    row = db.query(ZIPS).get(id)

    # request the weather at that location
    weather = requests.get("https://api.darksky.net/forecast/a84956e54a244e49b63db906daf2fe67/{},{}".format(row.latitude,row.longtitude)).json()["currently"]
    # convert time to readable content and humidity to percentage
    weather['time'] = datetime.datetime.fromtimestamp(
        int(weather['time'])
    ).strftime('%Y-%m-%d %H:%M:%S')
    weather['humidity'] = int(weather['humidity']*100)

    print(weather)
    return render_template("zip.html", row=row, weather=weather)

@app.route("/api/<string:zip>")
def api_zip(zip):
    row = db.query(ZIPS).filter(ZIPS.zipcode == zip).first()
    print ('row:')
    print (row)
    if row is None:
        return jsonify({"error": "ZIPCODE not found"}), 405

    return jsonify({
            "place_name": row.city,
            "state": row.state,
            "latitude": str(row.latitude),
            "longitude": str(row.longtitude),
            "zip": row.zipcode,
            "population": str(row.population),
            "check_ins": str(row.checkins)
        })

@app.route("/checkin",  methods=["POST"])
def checkin():
    id = request.args.get('id')

    # check user and location combination does not exist
    query = db.query(Comments).filter(Comments.idlocation==id, Comments.userid==session['user_id']).first()

    if query is None:
        row = db.query(ZIPS).get(id)
        row.checkins+=1
        db.commit()

        # retrieve the comment
        com = request.form.get('comment')
        # add log to comments db
        comment = Comments(idlocation=id, location=row.city, userid=session['user_id'], comment=com)
        db.add(comment)
        db.commit()
        return redirect(url_for("zip", id=id))
    # user is not allowed to add another checkin
    else:
        print ("User was not allowed to add comment.")
        return redirect(url_for("zip", id=id))


@app.route("/logout")
def logout():
    # forget current user_id
    db.remove()

    # redirect user to login Form
    return redirect(url_for("login"))

@app.route("/register", methods=["GET", "POST"])
def register():

    # allow registration
    if request.method == "GET":
        return render_template("register.html")

    # process registration
    elif request.method == 'POST':

        # collect username and passwords from registration
        uname = request.form.get("username")
        pw1 = request.form.get("password")
        pw2 = request.form.get("rePassword")

        # check validity of username and passwords
        if not uname:
            return apology("must provide username")
        elif not pw2 or not pw2:
            return apology("must provide password twice")
        elif not pw1 == pw2:
            return apology("passwords must match")
        if uname in db.query(UserLogin.name):
            return apology("username already exists")

        else:
            userlogin = UserLogin(name=uname, password=pw1)
            db.add(userlogin)
            db.commit()

        # redirect user to login form
        return redirect(url_for("login"))
