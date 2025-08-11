from flask import Flask

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# variable containing a WSGI-compliant object.
app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello, World!'


if __name__ == '__main__':
    # This is used when running locally only. When deploying to App Engine,
    # a webserver process such as Gunicorn will serve the app.
    app.run(host='127.0.0.1', port=8080, debug=True)