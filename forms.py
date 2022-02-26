from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, BooleanField
from wtforms.validators import InputRequired, Optional, NumberRange, URL




class PetForm(FlaskForm):
    """Form for adding a pet"""

    name = StringField(
        "Pet Name", validators=[InputRequired()])

    species = SelectField(
        "Species", choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")])

    photo_url = StringField(
        "Photo URL", validators=[Optional(), URL()])

    age = IntegerField(
        "Age", validators=[Optional(), NumberRange(min=0, max=30)])

    notes = StringField(
        "Notes", validators=[Optional()])

    available = BooleanField(
        "Available", default=True)



class EditPetForm(FlaskForm):
    """Form for editing pet details"""
    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()],
    )

    notes = StringField(
        "Notes",
        validators=[Optional()],
    )

    available = BooleanField("Available")
