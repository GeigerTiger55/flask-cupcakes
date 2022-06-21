from wtforms import StringField, SelectField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Optional


class CupcakeForm(FlaskForm):
    """Form for adding cupcakes."""

    flavor = StringField(
        "Flavor",
        validators=[InputRequired()],
        name="flavor",
    )

    size = StringField(
        "Size",
        validators=[InputRequired()],
        name="size",
    )

    rating = SelectField(
        "Rating",
        choices = [("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5")],
        validators=[InputRequired()],
        name="rating",
    )

    image = StringField(
        "Cupcake Picture URL",
        validators=[Optional()],
        name="image",
    )