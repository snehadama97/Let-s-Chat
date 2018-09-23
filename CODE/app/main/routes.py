from flask import session, redirect, url_for, render_template, request
from . import main
from .forms import LoginForm
import pickledb

db = pickledb.load("db.dat",False)



@main.route('/', methods=['GET', 'POST'])
def index():
    print(request.form)
    """Login form to enter a room."""
    form = LoginForm()
    if request.method == "POST":
        _f = db.get(request.form.get("room"))
        if _f:
            if _f == request.form["password"]:
                session['name'] = request.form["name"]
                session['room'] = request.form["room"]
                return redirect(url_for(".chat"))
            else:
                return render_template('index.html', form=form)
        else:
            db.set(request.form.get("room"),request.form["password"])
            session['name'] = request.form["name"]
            session['room'] = request.form["room"]
            return redirect(url_for(".chat"))

    elif request.method == 'GET':
        form.name.data = session.get('name', '')
        form.room.data = session.get('room', '')
    return render_template('index.html', form=form)


@main.route('/chat')
def chat():
    """Chat room. The user's name and room must be stored in
    the session."""
    name = session.get('name', '')
    room = session.get('room', '')
    if name == '' or room == '':
        return redirect(url_for('.index'))
    return render_template('chat.html', name=name, room=room)
