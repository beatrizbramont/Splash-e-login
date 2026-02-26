import os
from flask import Flask
from dotenv import load_dotenv

from extensions import mail
from controller.auth_controller import auth_bp
from controller.page_controller import page_bp
from model.user_model import create_users_table
from model.otp_model import create_otp_table

load_dotenv()

base_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(base_dir, "../templates"),
    static_folder=os.path.join(base_dir, "../static")
)

# CONFIG MAILTRAP
app.config['MAIL_SERVER'] = os.getenv("MAIL_SERVER")
app.config['MAIL_PORT'] = int(os.getenv("MAIL_PORT"))
app.config['MAIL_USERNAME'] = os.getenv("MAIL_USERNAME")
app.config['MAIL_PASSWORD'] = os.getenv("MAIL_PASSWORD")
app.config['MAIL_USE_TLS'] = os.getenv("MAIL_USE_TLS") == "True"
app.config['MAIL_USE_SSL'] = os.getenv("MAIL_USE_SSL") == "True"

mail.init_app(app)

create_users_table()
create_otp_table()

app.register_blueprint(auth_bp)
app.register_blueprint(page_bp)

if __name__ == "__main__":
    app.run(debug=True)