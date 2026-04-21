import os
import logging

from urlshortener import create_app

app = create_app()

if __name__ == '__main__':
    logging.getLogger("werkzeug").setLevel(logging.ERROR)
    print("LinkSwift is running at http://127.0.0.1:5000", flush=True)
    try:
        from waitress import serve
    except ImportError:
        app.run(debug=os.getenv('FLASK_DEBUG') == '1', use_reloader=False)
    else:
        serve(app, host='127.0.0.1', port=5000, _quiet=True)
