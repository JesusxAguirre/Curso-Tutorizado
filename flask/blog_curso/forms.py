from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
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
                            widget=TextArea(),
                            validators=[DataRequired(),
                                        Length(max=200)])

    submit = SubmitField("enviar_post")


class LoginForm(FlaskForm):

    email = StringField(
        "email",
        validators=[DataRequired(),
                    Email()])

    password = PasswordField(
        "password",
        validators=[DataRequired(),
                    Length(max=12)]
    )

    remember_me = BooleanField("Recuerdame")

    submit = SubmitField("iniciar_sesion")


class RegistroForm(FlaskForm):
    usuario = StringField(
        "usuario",
        validators=[DataRequired(),
                    Email()])

    password = PasswordField(
        "password",
        validators=[DataRequired(),
                    Length(max=12)]
    )

    nombre = StringField(
        "nombre",
        validators=[DataRequired(),Length(max=12)]
    )
    


    submit = SubmitField("registrar usuario")
