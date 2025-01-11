# Nutrition-App
## Instructions
Run ./run_server.sh for full set up and to run the Flask application

## What is Flask?
**Flask** is a micro-web Python framework. A **web framework** is a piece of software designed to support the development of web applications. 

More specifically, Flask is a ***WSGI (Web Server Gateway Interface)** framework, which means Flask relies on the WSGI external library to provide a way for web servers to pass requests to web applications, along with the Jinja2 template engine to create output documents. 

## How do we use Flask?
Django might have a more specific process when we create applications, such as defining a model, creating a view and template associated with the model, defining the urls in the associated file, configuring the settings to include the application, etc...

Flask is a little simpler. We essentially have one python file (not restricted to, of course), where we start the application, and set the url routes with their associated functions that render the templates (or some other function). The main code we want to pay attention to is defined below:
```
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('URL_GOES_HERE', methods=[]) # What would go inside methods is dependent on whether you are adding an element('POST'), retrieving an element('GET'), or deleting an element ('DELETE')

def function_name():
    return render_template('template_name')

if __name__ == '__main__':
    app.run(debug=True)
```

As we build on this application, we will most likely be adding more functions with their associated HTML/CSS files as well as their application routes. 