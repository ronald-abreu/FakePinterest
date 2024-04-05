from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from fakepinterest.models import Usuario


class FormLogin(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    senha = PasswordField("Password", validators=[DataRequired()])
    botao_confirmacao = SubmitField("Login")

class FormCriarConta(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    username = StringField("Username", validators=[DataRequired()])
    senha = PasswordField("Password", validators=[DataRequired(), Length(6, 20)])
    confirmacao_senha = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("senha")])
    botao_confirmacao = SubmitField("Register")

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email)