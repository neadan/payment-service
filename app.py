from flask import Flask, render_template
import os



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql+psycopg2://{os.environ['POSTGRES_USER']}:" \
                                        f"{os.environ['POSTGRES_PASSWORD']}" \
                                        f"@purchase-db/{os.environ['POSTGRES_DB']}"


@app.route('/api/v1/home')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run()