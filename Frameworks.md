Python most popular frameworks

1. **Django framework**
2. *******************
   A high-level web framework that encourages rapid development and clean, pragmatic design.  It includes an ORM (Object-Relational Mapping) system for database access.

   eg:
   #models.py
   from django.db import models

   class Book(models.Model):
       title = models.ChaarField(max_length=100)
       author = models.CharField(max_length=50)

    # views.py
    from django.shortcuts import render
    from .models import Book

    def book_list(request):
        books = Book.objects.all()
        return render(request, 'books/book_list.html', {'books': books})

3. **Flask**
   ********
   A lightweight and flexible micro-framework for web development.  Flask is often used for building small to medium-sized web applications.

   eg
   from flask import Flask, render_template
   app = Flask(__name__)

   @app.route('/')
   def index():
       return render_template('index.html')

    if __name__ == '__main__':
        app.run(debug=True)

3. **Pyramid**
   **********
   A full-featured, modular web framework for building web applications.  It is designed to be flexible and allows developers to choose the components they want to use.

   eg

   from pyramid.config import Configurator
   from pyramid.response import Response

   def hello_world(request):
       return Response('Hello World!')

    config = Configurator()
    config.add_route('hello', '/hello')
    config.add_view(hello_world, route_name='hello')
    app = config.make_wsgi_app()

4. **FastAPI**
   **********
   A modern, fast(high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.

   eg
   from fastapi import FastAPI

   app = FastAPI()

   @app.get("/")
   def read_root():
       return {"Hello": "World"}

5. **Tornado   **
   **************   
   A web framework and asynchronous networking library.  It's particularly suitable for handling long-lived network connections.

   eg

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, World")
def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

6. **CherryPy**
   ***********
   An object-oriented web framework that allows developers to build web applications in a similar way to writing python progams.

eg

import cherrypy

class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return "Hello, World!"

if __name__ == '__main__':
cherrypy.quickstart(HelloWorld())


7.** Bottle**
   ***********
   A simple and lightweight micro-framework for small web applications.  It is distributed as a single-file module.

eg

from bottle import route, run

@route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)

8. ** Dash (by Plotly)**
************************
A productive Python framework for building web applications with complex interactions. It's often used for creating data visualizations.

eg.

import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div(childern=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montreal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)

9. **Scrapy**
    *********

    Am open-source and collaborative web crawling framework for Python.  It's commonly used for data mining, data scraping, and extracting structured data from websites.

eg
  # bash
scrapy startproject myproject
cd myproject
scrapy genspider example example.com
scrapy crawl example

10.  **Tensorflow and pyTorch**
    **************************
    While not traditional web frameworks, these are popular frameworks for machine learning and deep learning, respectively.

    eg
    **TensorFlow**
    import tensorflow as tf
    from tensorflow.keras import layers, models

    #Load the CIFAR-10 dataset
    (train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.cifar10.load_data()

    #Define the model
    model = models.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
        layers.MaxPooling2D((2,2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        layers.Dense(10, actigation='softmax')
    ])

   # Compile the model
   model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

   # Train the model
   model.fit(train_images, train_labels, epochs=10, validation_data=(test_images, test_labels))

   #Evaluate the model
   test_loss, test_acc = model.evaluate(test_images, test_labels)
   print(f'Test accuracy: {test_acc}')

   # PyTorch
   import torch
   import torch.nn as nn
   import torch.optim as optim
   import numpy as np

   #Generate random data
   x = torch.tensor(np.random.rand(100, 1), dtype=torch.float32)
   y = 3 * x + 2 + 0.1 * torch.randn(100, 1)

   # Define a simple linear regression model
   model = nn.Linear(1, 1)
   criterion = nn.MSELoss()
   optimizer = optim.SGD(model.parameters(), lr=0.01)

   # Train the model
   for epoch in range(100):
       optimizer.zero_grad()
       outputs = model(x)
       loss = criterion(outputs, y)
       loss.backward()
       optimizer.step()

    #Print the learned parameters
    print("Learned parameters: ", model.weight.item(), model.bias.item())

    