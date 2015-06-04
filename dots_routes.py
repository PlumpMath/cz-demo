from flask import render_template, jsonify, redirect
import random
import logic

ALL_PAGES = ['simple', 'hal', 'dots', 'stack', 'blink', 'shift', 'spin']

def route(app):
    @app.route('/page/<name>')
    def page(name):
        return render_template('page.html', name=name)

    # A special URL which redirects to a random display page:

    @app.route('/random')
    def random_page():
        return redirect("/page/{name}".format(name=random.choice(ALL_PAGES)))

    @app.route('/data/simple/<int:counter>')
    def simple(counter):
        print("COUNTER", counter)
        return jsonify({'result': [{'rgb': [0, 0, 0],
                                    'x': 0.5,
                                    'y': 0.5,
                                    'r': 1,
                                    'key': counter}]})

    @app.route('/data/hal/<int:counter>')
    def hal(counter):
        return jsonify({'result': [{'rgb': [random.random() for _ in range(3)],
                                    'x': 0.5,
                                    'y': 0.5,
                                    'r': 0.5 + 2.0 * random.random(),
                                    'key': 0}]})

    @app.route('/data/dots/<int:counter>')
    def dots(counter):
        return jsonify({'result': logic.makeDots()})

    @app.route('/data/stack/<int:counter>')
    def stack(counter):
        return jsonify({'result': logic.makeStack(counter)})

    @app.route('/data/blink/<int:counter>')
    def blink(counter):
        return jsonify({'result': logic.makeBlink(True)})

    @app.route('/data/shift/<int:counter>')
    def shift(counter):
        return jsonify({'result': logic.makeBlink(False)})

    @app.route('/data/spin/<int:counter>')
    def spin(counter):
        return jsonify({'result': logic.makeSpin(counter)})
