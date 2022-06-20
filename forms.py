from wtforms import StringField, SelectField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired


class CupcakeForm(FlaskForm):
    """Form for adding cupcakes."""

    flavor = StringField(
        "Flavor",
        validators=[InputRequired()]
    )

    size = StringField(
        "Size",
        validators=[InputRequired()]
    )

    rating = SelectField(
        "Rating",
        choices = [("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5")],
        validators=[InputRequired()]
    )

    image = StringField(
        "Cupcake Picture URL",
        validators=[InputRequired()]
    )