"""Forms for playlist app."""

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, URL


class CupcakeForm(FlaskForm):
    """Form for adding cupcakes."""

    flavor = StringField("Cupcake Flavor", validators=[InputRequired()])
    size = StringField("Cupcake Size", validators=[InputRequired()])
    rating = IntegerField("Cupcake Rating", validators=[InputRequired()])
    image = StringField("Cupcake Image URL", validators=[InputRequired(), URL()])

