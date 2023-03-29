from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length
from wtforms.widgets import TextArea

class SignupForm(FlaskForm):

    name = StringField(
        "nombre",
        validators=[DataRequired(),
                    Length(max=25)]
    )
    password = PasswordField(
        "password",
        validators=[DataRequired(),
                    Length(max=12)]
    )
    email = StringField(
        "email",
        validators=[DataRequired(),
                    Email()])
    submit = SubmitField("envio_formulario")


class PostForm(FlaskForm):

    titulo = StringField(
        "titulo",
        validators=[DataRequired(),
                    Length(max=15)])

    contenido = StringField("contenido",
                            widget = TextArea(),
                            validators=[DataRequired(),
                                        Length(max=200)])
    
    submit = SubmitField("enviar_post")
