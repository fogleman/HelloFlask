# Hello Flask

A boiler-plate starting point for a Flask web application, including SQLAlchemy and WTForms.

## Dependencies

    pip install Flask
    pip install Flask-SQLAlchemy
    pip install Flask-WTF

## Customizations

**Be sure to set a `SECRET_KEY` in hello/config.py** ... you can generate one like this:

    import uuid
    print uuid.uuid4().hex

## Running

    python main.py

## Screenshot

![](https://raw.github.com/fogleman/HelloFlask/master/screenshot.png)