import os

from flask import Flask, render_template


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.environ['POSTGRES_USER']}:" \
                                            f"{os.environ['POSTGRES_PASSWORD']}" \
                                            f"@payment-db/{os.environ['POSTGRES_DB']}"
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app


app = create_app()


@app.route('/api/v1/home')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run()