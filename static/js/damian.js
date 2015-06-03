// Generated by CoffeeScript 1.8.0
(function() {
  var counter, oneCycle, rgb_str, svg;

  svg = d3.select("div#inner").append("svg").attr("width", 600).attr("height", 600);

  rgb_str = function(d) {
    var rgbs;
    rgbs = d.rgb.map(function(v) {
      return (v * 255).toFixed();
    });
    return "rgb(" + (rgbs.join()) + ")";
  };

  counter = 0;

  oneCycle = function(path) {
    return d3.json(path + "/" + counter, function(error, json) {
      var c, circle;
      if (error) {
        return console.warn(error);
      } else {
        circle = svg.selectAll("circle");
        c = circle.data(json.result, function(d) {
          return +d.key;
        });
        c.transition().duration(1000).ease("elastic").attr("cx", function(d) {
          return d.x * 600;
        }).attr("cy", function(d) {
          return d.y * 600;
        }).attr("r", function(d) {
          return d.r * 40;
        }).attr("fill", rgb_str);
        c.enter().append("circle").attr("cx", function(d) {
          return d.x * 600;
        }).attr("cy", function(d) {
          return d.y * 600;
        }).attr("r", 0).transition().duration(1000).attr("r", function(d) {
          return d.r * 40;
        }).attr("fill", rgb_str);
        c.exit().transition().duration(1000).attr("r", 0).remove();
        return counter = counter + 1;
      }
    });
  };

  this.go = function(path) {
    setInterval((function() {
      return oneCycle(path);
    }), 3000);
    setTimeout((function() {
      return window.open("/random", "_self");
    }), 10000);
    return oneCycle(path);
  };

}).call(this);
