from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, BooleanField
from wtforms.validators import DataRequired, NumberRange

class TaskForm(FlaskForm):
    task_type = StringField('Task Type', validators=[DataRequired()])
    companies = StringField('Companies')
    required_time = IntegerField('Required Time (minutes)', validators=[DataRequired(), NumberRange(min=1)])
    order_to = StringField('Order To', validators=[DataRequired()])
    delegation = BooleanField('Delegation')
    ordered_by = StringField('Ordered by')
    submit = SubmitField('Create Task')

class TaskTypeForm(FlaskForm):
    name = StringField('Task Type', validators=[DataRequired()])
    submit = SubmitField('Add Task Type')

class CompanyForm(FlaskForm):
    name = StringField('Company', validators=[DataRequired()])
    submit = SubmitField('Add Company')

# vim:ts=2:sts=2:sw=2:et
