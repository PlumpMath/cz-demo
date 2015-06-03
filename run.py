from flask import Flask, render_template, jsonify
import os, random
import logic

app = Flask(__name__)

@app.route('/page/<name>')
def page(name):
    return render_template('index.html', name=name)

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

app.run(host='0.0.0.0', port=8080, debug=True)
