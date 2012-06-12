# Hello Flask

A boiler-plate starting point for a Flask web application, including SQLAlchemy, WTForms and Bootstrap.

## Demo

http://mfogleman.webfactional.com/hello/

## Dependencies

    pip install Flask
    pip install Flask-SQLAlchemy
    pip install Flask-WTF

## Customizations

**Be sure to set a `SECRET_KEY` in hello/config.py** ... you can generate one like this:

    import uuid
    print uuid.uuid4().hex

## Modules

Although it is possible for a Flask app to be contained entirely within a single Python module, this project splits different functionality into different modules to facilitate maintainability. Below is a description of each module.

- `__init__.py` - Constructs the Flask app object and configures it. Imports the other modules to emulate a single-module application.
- `config.py` - Contains the app configuration.
- `forms.py` - Contains WTForms Form objects for use in views and templates.
- `hooks.py` - Contains Flask and Jinja helper methods.
- `models.py` - Contains the database model classes for SQLAlchemy.
- `views.py` - Contains the app views.

## Running

    python main.py

## Screenshot

![](https://raw.github.com/fogleman/HelloFlask/master/screenshot.png)
