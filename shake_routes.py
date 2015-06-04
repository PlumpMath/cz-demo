from flask import render_template, jsonify
import random, os
import shake_logic

corpus = shake_logic.filesToDict(['data/' + f for f in os.listdir('data')])

playWords = shake_logic.allPlayWords(corpus)

print("Random play word: " + random.choice(list(playWords)))

searchWords = ["love", "hate",
               "king", "queen",
               "country", "kingdom",
               "army", "navy",
               "revenge", "justice",
               "romeo", "asjasjasjasj"]

def route(app):
    @app.route('/shakespeare')
    def shakespeare():
        return render_template('shake.html', searchWords=searchWords)

    @app.route('/shake/<word>')
    def shake(word):
        r = [{'value': i, 'text': name}
             for name, i in shake_logic.freqAnalyzer(corpus, word).iteritems()
        ]

        return jsonify({'result': r})
