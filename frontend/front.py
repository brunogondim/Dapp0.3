import logging
import time
from flask import Flask, render_template, request, redirect, flash
from models.forms import InsertForm, SelectForm, UpdateForm, DeleteForm
from controllers.addinput import tx_hash
from controllers.query import inspect

app = Flask(__name__)
app.config["SECRET_KEY"] = "secretkey"
app.config["DEBUG"] = True
app.logger.setLevel(logging.INFO)

def hex2str(hex):
    return bytes.fromhex(hex[2:]).decode("utf-8")

def str2hex(str):
    return "0x" + str.encode("utf-8").hex()

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route('/insert', methods=['GET', 'POST'])
def insert():
    insert_form = InsertForm()

    if insert_form.validate_on_submit():
        # statement = str2hex(insert_form.insert_statement())
        # tx_hash(statement)
        flash("Added data.", 'success')
    # else:
    #     flash("Error.", 'error')

    return render_template('insert.html', insert_form=insert_form)

@app.route('/select', methods=['GET', 'POST'])
def select():
    select_form = SelectForm()
    payload_list = []

    if select_form.submit.data:
        payload_list = select_form.inspect(select_form.select_statement())

    return render_template('select.html', select_form=select_form, payload_list=payload_list)


@app.route('/update', methods=['GET', 'POST'])
def update():
    update_form = UpdateForm()

    if update_form.submit.data and update_form.validate():
        statement = str2hex(update_form.update_statement())
        tx_hash(statement)
        flash("Updated data", 'success')
    # else:
    #     flash("Error.", 'error')

    return render_template('update.html', update_form=update_form)


@app.route('/delete', methods=['GET', 'POST'])
def delete():
    delete_form = DeleteForm()

    if delete_form.submit.data and delete_form.validate():
        statement = str2hex(delete_form.delete_statement())
        tx_hash(statement)
        flash("Deleted data.", 'success')
    # else:
    #     flash("Error.", 'error')

    return render_template('delete.html', delete_form=delete_form)