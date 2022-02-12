from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import ninja
from flask_app.models import dojo


# CREATE controller

@app.route("/new_ninja")
def add_new_ninja():
    return render_template('/new_ninja.html', dojos = dojo.Dojo.get_all_dojos())

@app.route("/ninjas/create", methods = ['POST'])
def create_ninja():
    ninja.Ninja.create_ninjas(request.form)
    return redirect('/')


# READ controller

@app.route('/')
def index_():
    all_ninjas = ninja.Ninja.get_all_ninjas()
    return render_template('index.html', ninjas = all_ninjas)


# UPDATE controller

@app.route('/ninjas/update/<id>')
def update_form(id):
    this_ninja = ninja.Ninja.get_user_by_id(id)
    return render_template('update_ninja.html', ninja = this_ninja)

@app.route('/ninjas/update/process', methods = ['POST'])
def process_update():
    ninja.Ninja.update_ninja(request.form)
    return redirect('/')


# DELETE controller

@app.route('/ninjas/delete/<id>')
def delete_the_ninja(id):
    ninja.Ninja.delete_ninja(id)
    return redirect('/')

@app.route('/ninjas/profile/<id>')
def profile(id):
    ninja.Ninja.get_user_by_id(id)