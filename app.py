from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data store
books = [{
        "id": 1,
        "title": "Python Programming",
        "author": "John Doe"
    },
    {
        "id": 2,
        "title": "Java Programming",
        "author": "Jane Doe"
    },
    {
        "id": 3,
        "title": "C Programming",
        "author": "Jim Doe"
    }]

# Create a book
@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    book = {
        'id': len(books) + 1,
        'title': data['title'],
        'author': data['author']
    }
    books.append(book)
    return jsonify(book), 201

# Read all books
@app.route('/books', methods=['GET'])
def get_all_books():
    return jsonify(books)

# Read a specific book
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        return jsonify(book)
    return jsonify({'message': 'Book not found'}), 404

# Update a book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        data = request.get_json()
        book['title'] = data['title']
        book['author'] = data['author']
        return jsonify(book)
    return jsonify({'message': 'Book not found'}), 404

# Delete a book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        books.remove(book)
        return jsonify({'message': 'Book deleted'})
    return jsonify({'message': 'Book not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)