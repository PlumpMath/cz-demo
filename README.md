`-*- mode: markdown; mode: visual-line; mode: adaptive-wrap-prefix; -*-`

# `cz-demo`

This is a quick port of one of the Ravensbourne CodeZoners exercises into a "booth" format, cycling between various display patterns. It's Heroku-friendly. For the hell of it, we've also back-ported the Javascript code into CoffeeScript. 

The pattern frames are fetched from the (Python) server, which is a rather daft thing to do - much better to hold all the logic in the browser - but it was serving as an exercise in JSON API design (and Python coding).

## Deployment

- The CoffeeScript sources are in directory `static/coffee`; to automatically compile these into Javascript, install CoffeeScript (`sudo npm install -g coffee-script`) - which might require the `node` command in order to run (via `sudo apt-get install nodejs-legacy`) and then:

        coffee -c -w -o static/__js/ static/coffee/
        
  This will auto-watch and compile changed files. (It'll need to be relaunched if any new files are added.) Note that `coffee/*.coffee` works better as a source if you're an Emacs user (otherwise the auto-watch gets confused by Emacs auto-save files).

- Rename the app from `cz-demo` to something unique (modifying the `Procfile` accordingly)

- In the Heroku instance, set the environment variable `DEPLOYED` to `yes`, to prevent the main script from trying to spin up a Flask server
