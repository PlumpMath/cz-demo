from flask import Flask, render_template
import os

import dots_routes, shake_routes

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
                           pages=dots_routes.ALL_PAGES)

dots_routes.route(app)
shake_routes.route(app)

if "DEPLOYED" in os.environ and os.environ["DEPLOYED"] == "yes":
    print "not starting up Flask"
else:
    app.run(host='0.0.0.0', port=8080, debug=True)
