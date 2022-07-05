import logging
from flask import Flask, render_template, request, redirect
from models.forms import InsertForm, SelectForm, UpdateForm, DeleteForm
from controllers.addinput import tx_hash
from controllers.notice import notice

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
    select_form = SelectForm()
    update_form = UpdateForm()
    delete_form = DeleteForm()

    if insert_form.submit.data and insert_form.validate():
        statement = str2hex(insert_form.insert_statement())
        tx_hash(statement)
        print("insert")

    return render_template('addinput.html', insert_form=insert_form, select_form=select_form, update_form=update_form, delete_form=delete_form)

@app.route('/select', methods=['GET', 'POST'])
def select():
    insert_form = InsertForm()
    select_form = SelectForm()
    update_form = UpdateForm()
    delete_form = DeleteForm()

    if select_form.submit.data and select_form.validate():
        statement = str2hex(select_form.select_statement())
        tx_hash(statement)
        print("select")

    return render_template('addinput.html', insert_form=insert_form, select_form=select_form, update_form=update_form, delete_form=delete_form)


@app.route('/update', methods=['GET', 'POST'])
def update():
    insert_form = InsertForm()
    select_form = SelectForm()
    update_form = UpdateForm()
    delete_form = DeleteForm()

    if update_form.submit.data and update_form.validate():
        statement = str2hex(update_form.update_statement())
        tx_hash(statement)
        print("update")

    return render_template('addinput.html', insert_form=insert_form, select_form=select_form, update_form=update_form, delete_form=delete_form)


@app.route('/delete', methods=['GET', 'POST'])
def delete():
    insert_form = InsertForm()
    select_form = SelectForm()
    update_form = UpdateForm()
    delete_form = DeleteForm()

    if delete_form.submit.data and delete_form.validate():
        statement = str2hex(delete_form.delete_statement())
        tx_hash(statement)
        print("delete")

    return render_template('addinput.html', insert_form=insert_form, select_form=select_form, update_form=update_form, delete_form=delete_form)