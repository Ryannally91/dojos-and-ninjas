from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import dojo


@app.route('/')
def index():
    return render_template('index.html', list_dojos=dojo.Dojo.get_all_dojos() )

@app.route('/create_dojo', methods=['POST'])
def create():
    dojo.Dojo.create_dojo(request.form)
    return redirect('/')

@app.route('/dojo/<id>') 
def get_dojo(id):
    this_dojo= dojo.Dojo.get_one_dojo(id)
    return render_template('display_dojo.html', dojo = this_dojo)

# @app.route('/delete_all')
# def delete_everything():
#     dojo.Dojo.delete_all_dojo()
#     return redirect('/')