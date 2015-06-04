var WIDTH = 600;
var HEIGHT = 600;
var RADIUS = Math.min(WIDTH, HEIGHT) / 2;

var OUTER_RADIUS = RADIUS - (WIDTH / 10);
var INNER_RADIUS = RADIUS - (WIDTH / 6);

var color = d3.scale.category20();

var svg = d3.select("div#inner").append("svg")
        .attr("width", WIDTH)
        .attr("height", HEIGHT)
        .append("g")
        .attr("transform", "translate(" + WIDTH / 2 + ", " + HEIGHT / 2 + ")");

function angle(d) {
    var a = (d.startAngle + d.endAngle) * 90 / Math.PI - 90;
    return a > 90 ? a - 180 : a;
}

function totalCount(data) {
    return data
        .map(function (x) { return x.value; })
        .reduce(function (x1, x2) { return x1 + x2; }, 0);
}

function makeArc() {
    return d3.svg.arc()
        .outerRadius(OUTER_RADIUS)
        .innerRadius(INNER_RADIUS);
}

function makePie() {
    return d3.layout.pie()
        .sort(null)
        .value (function (d) { return +d.value; });
}

function createArcs(g, arc) {
    g.append("path")
        .attr("d", arc)
        .style("fill", function (d, i) { return color(i); })
        .each(function(d) {
            console.log("enter on " + JSON.stringify(d));
            this._current = d.data;
        });
}

function createText(g, arc) {
    g.append("text")
        .attr("transform", function (d) {
            var t = "translate(" + arc.centroid(d) + ")";
            // Exercise: rotate text.
            var r = "rotate(" + angle(d) + ")";
            return t + r;
        })
        .attr("dy", ".35em")
        .style("text-anchor", "middle")
        .text(function (d) { return d.data.text; });
}

function transitionArcs(data, arc) {
    data.select("path")
        .transition()
        .delay(250)
        .duration(2000)
    /*.attr("d", arc)*/  /*linear tween: horrid!*/
        .attrTween("d", arcTween(arc));
}

function transitionText(data, arc) {
    /* Similar: move the text... (Also: change it, in case it's dynamic!) */
    data.select("text")
    // Exercise: no text if value is 0.
        .text(function (d) { if (d.data.value > 0) {
            return d.data.text;
        } else {
            return null;
        }})
    /*.transition()
     .duration(2000)*/
        .attr("fill-opacity", "0.0")
        .attr("transform", function (d) {
            var t = "translate(" + arc.centroid(d) + ")";
            // Exercise: rotate the text.
            var r = "rotate(" + angle(d) + ")";
            return t + r;
        })
        .transition()
        .duration(500)
        .delay(2250)
        .attr("fill-opacity", "1.0");
}

var arc = makeArc();

function go(word) {
    d3.json("/shake/" + word, function (error, json) {
        if (error) { return console.warn(error); }

        if (totalCount(json.result) == 0) {
            console.log("count is 0");
            svg.selectAll(".arc path")
                .transition()
                .duration(500)
                .attr("fill-opacity", "0.0");
            svg.selectAll(".arc text")
                .transition()
                .duration(500)
                .attr("fill-opacity", "0.0");
        } else {
            svg.selectAll(".arc path")
                .transition()
                .duration(250)
                .attr("fill-opacity", "1.0");

            var pie = makePie();

            var data = svg.selectAll(".arc")
                .data(pie(json.result));

            g = data.enter()
                .append("g")
                .attr("class", "arc");

            createArcs(g, arc);
            createText(g, arc);

            transitionArcs(data, arc);
            transitionText(data, arc);

            data.exit().remove();
        }
    });
}

function arcTween(arc) {
    return function (a) {
        console.log("_current: " + this._current);
        var i = d3.interpolate(this._current, a);
        this._current = i(0);
        return function(t) {
            return arc(i(t));
        };
    };
}

// Hack for the type-in field (fiddle at http://jsfiddle.net/pxfunc/5kpeJ/):

$("#type-in").bind('input', function() {
    var text = $(this).val();
    // Boo...!:
    if (text == "") { text = "*BOGUS*"; }
    go(text);
});
