from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, TimeField, SelectField, validators
from wtforms.validators import DataRequired
import csv

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    map = URLField(label='Location', validators=[DataRequired(), validators.URL()])
    open = TimeField(label='Opens At', validators=[DataRequired()])
    close = TimeField(label='Closes At', validators=[DataRequired()])
    coffee = SelectField(
        label='Coffee Rating',
        choices=[
            ('value1', '☕️☕️☕️☕️☕️'),
            ('value2', '☕️☕️☕️☕️'),
            ('value3', '☕️☕️☕️'),
            ('value4', '☕️☕️'),
            ('value5', '☕️')
        ]
    )
    wifi = SelectField(
        label='Wifi Rating',
        choices=[
            ('value1', '💪💪💪💪💪'),
            ('value2', '💪💪💪💪'),
            ('value3', '💪💪💪'),
            ('value4', '💪💪'),
            ('value5', '💪')
        ]
    )
    power = SelectField(
        label='Power Rating',
        choices=[
            ('value1', '🔌🔌🔌🔌🔌'),
            ('value2', '🔌🔌🔌🔌'),
            ('value3', '🔌🔌🔌'),
            ('value4', '🔌🔌'),
            ('value5', '🔌')
        ]
    )
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        return "Success!"
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
