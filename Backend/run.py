from flask import Flask
from app.views import *
from app.database import init_app

#inicializacion del proyecto Flask
app = Flask(__name__)

init_app(app)

app.route('/', methods=['GET'])(index)
app.route('/api/books/', methods=['GET'])(get_all_books)
app.route('/api/books/<int:book_id>', methods=['GET'])(get_book)
app.route('/api/books/', methods=['POST'])(create_book)
app.route('/api/books/<int:movie_id>', methods=['PUT'])(update_book)

if __name__=='__main__':
    app.run(debug=True)