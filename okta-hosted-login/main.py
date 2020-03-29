# Base
import uuid

# Flask
from flask import Flask, render_template, url_for, redirect, jsonify, request, session
from flask_oidc import OpenIDConnect
from flask_cors import CORS

#db
import dbUtils
from flask import g


app = Flask(__name__)
app.config.update({
    'SECRET_KEY': 'SomethingNotEntirelySecret',
    'OIDC_CLIENT_SECRETS': './client_secrets.json',
    'OIDC_ID_TOKEN_COOKIE_SECURE': False,
    'OIDC_SCOPES': ["openid", "profile", "email"],
    'OIDC_CALLBACK_ROUTE': '/authorization-code/callback'
})

oidc = OpenIDConnect(app)




@app.route("/")
@oidc.require_login
def home():
    # dbUtils.create_connection('testDb.db')
    info = oidc.user_getinfo(["sub", "name", "email"])
    hello()
    return render_template("home.html", profile=info, oidc=oidc)

def hello():
    print("here")
    g.db=dbUtils.get_db()
    # print(db)
    # cur = g.db.execute('CREATE TABLE t2 ("name"	TEXT)')
    # print(cur)
        # print(table)
    res=dbUtils.query_db('select * from users')
    print(res)
    # for user in res:
    #     print(user['name'], 'has the address', user['address'])


@app.route("/login")
@oidc.require_login
def login():
    return redirect(url_for("profile"))


@app.route("/profile")
@oidc.require_login
def profile():
    info = oidc.user_getinfo(["sub", "name", "email"])

    return render_template("profile.html", profile=info, oidc=oidc)


@app.route("/logout", methods=["POST"])
def logout():
    oidc.logout()
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)
