from flask import Flask, session, redirect, url_for, escape, request
from flask import render_template
from gothonweb import planisphere

app = Flask(__name__)

@app.route("/")
def index():
    # this is used to "setup" the session with starting values
    session['room_name'] = planisphere.START
    return redirect(url_for("game"))

@app.route("/game", methods = ['POST', 'GET'])
def game():
    room_name = session.get('room_name', planisphere.START)

    if request.method == 'GET':

        if room_name:
            room = planisphere.load_room(room_name)
            return render_template("show_room.html", room = room)
        else:
            # why is there here? do you need it?
            return render_template("you_died.html")

    else:

        if room_name:
            room = planisphere.load_room(room_name)

        action = request.form.get('action')

        next_room = None
        if room and action:
            next_room = room.go(action)

        if next_room:
            session['room_name'] = planisphere.name_room(next_room)
        else:
            session['room_name'] = planisphere.name_room(room)

        return redirect(url_for("game"))

app.secret_key = "a"

if __name__ == '__main__':
    app.run(threaded = True)
