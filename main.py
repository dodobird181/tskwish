from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


from models import Embedding, Float, Vector, VectorData

embedding = Embedding.create(text='Hey thar!')
print(embedding.text)
print(len(embedding.vector.as_list()))

embedding = Embedding.create(text='Pee pee?')
print(embedding.text)
print(len(embedding.vector.as_list()))

embedding = Embedding.create(text='Pee pee poo poo poo!')
print(embedding.text)
print(len(embedding.vector.as_list()))
