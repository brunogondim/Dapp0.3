from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DecimalField, RadioField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, NumberRange
import requests
import json


def hex2str(hex):
    return bytes.fromhex(hex[2:]).decode("utf-8")

def str2hex(str):
    return "0x" + str.encode("utf-8").hex()

class InsertForm(FlaskForm):
    age = IntegerField("Age", validators=[DataRequired(), NumberRange(min=0, max=100)])
    sex = SelectField("Sex", choices=["Male", "Female"], validators=[DataRequired()])
    bmi = DecimalField("BMI", validators=[DataRequired(), NumberRange(min=0, max=100)])
    children = IntegerField("Children", validators=[DataRequired()])
    smoker = SelectField("Smoker", choices=["Yes", "No"], validators=[DataRequired()])
    region = SelectField("Region", choices=["Northeast", "Northwest", "Southeast", "Southwest"], validators=[DataRequired()])
    charges = DecimalField("Charges", validators=[DataRequired()])
    submit = SubmitField("Submit")

    def insert_statement(form):
        data = []
        for field in form:
            data.append(str(field.data).lower())
        statement = f"INSERT INTO Medical VALUES ({str(data[:-2])[1:-1]})"
        return str(statement)


class SelectForm(FlaskForm):    
    age = IntegerField("age", validators=[NumberRange(min=0, max=100)])
    sex = SelectField("sex", choices=["-", "Male", "Female"])
    bmi = DecimalField("bmi", validators=[NumberRange(min=0, max=100)])
    children = IntegerField("children") # when is 0, dont work (TO DO)
    smoker = SelectField("smoker", choices=["-", "Yes", "No"])
    region = SelectField("region", choices=["-", "Northeast", "Northwest", "Southeast", "Southwest"])
    charges = DecimalField("charges")

    submit = SubmitField("Submit")

    def select_statement(form):
        statement = "SELECT * FROM Medical WHERE " 
        data = []
        if form.sex.data == "-":
            form.sex.data = None
        if form.smoker.data == "-":
            form.smoker.data = None
        if form.region.data == "-":
            form.region.data = None
        for field in form:
            if field.data:
                data_field = (field.name, str(field.data).lower())
                data.append(data_field)
        data = data[:-2]
        for d in data:
            statement += d[0] + "=" + "'" + d[1] + "'" + " AND "
        statement = statement[0:-5]
        return str(statement)

    def inspect(form, statement):
        hex_input = str2hex(statement)
        report = requests.get(f"http://localhost:5002/inspect/{hex_input}")
        payload = hex2str(report.json()["reports"][0]["payload"])
        payload = json.loads(payload)
        print(payload)
        return payload


class UpdateForm(FlaskForm):
    attribute = SelectField("Attribute", choices=["Age", "Sex", "BMI", "Children", "Smoker", "Region", "Charges"], validators=[DataRequired()])
    new_value = StringField("New Value", validators=[DataRequired()])
    from_attribute = SelectField("From Attribute", choices=["Age", "Sex", "BMI", "Children", "Smoker", "Region", "Charges"], validators=[DataRequired()])
    from_value = StringField("From Value", validators=[DataRequired()])
    condition_attribute = SelectField("Condition Attribute", choices=["-", "Age", "Sex", "BMI", "Children", "Smoker", "Region", "Charges"])
    condition_value = StringField("Condition Value")
    submit = SubmitField("Submit")

    def update_statement(form):
        statement = f"UPDATE Medical SET {(form.attribute.data).lower()}='{(form.new_value.data).lower()}' FROM {(form.from_attribute.data).lower()}='{(form.from_value.data).lower()}'" 
        if form.condition_value.data:
            statement += f" WHERE {(form.condition_attribute.data).lower()}='{(form.condition_value.data).lower()}'"
        return str(statement)


class DeleteForm(FlaskForm):    
    age = IntegerField("Age", validators=[NumberRange(min=0, max=100)])
    sex = SelectField("Sex", choices=["----", "Male", "Female"])
    bmi = DecimalField("BMI", validators=[NumberRange(min=0, max=100)])
    children = IntegerField("Children")
    smoker = SelectField("Smoker", choices=["-", "Yes", "No"])
    region = SelectField("Region", choices=["-", "Northeast", "Northwest", "Southeast", "Southwest"])
    charges = DecimalField("Charges")

    submit = SubmitField("Submit")

    def delete_statement(form):
        form.submit.data = None
        statement = "DELETE FROM Medical WHERE " 
        data = []
        for field in form:
            if field.data:
                data_field = (field.name, str(field.data).lower())
                data.append(data_field)
        data = data[:-2]
        for d in data:
            statement += d[0] + "=" + d[1] + " AND "
        statement = statement[0:-4]
        return str(statement)