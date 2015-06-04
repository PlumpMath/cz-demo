# -*- coffee-tab-width: 4; -*-

WIDTH = 600
HEIGHT = 600
RADIUS = Math.min(WIDTH, HEIGHT) / 2

OUTER_RADIUS = RADIUS - (WIDTH / 10)
INNER_RADIUS = RADIUS - (WIDTH / 6)

color = d3.scale.category20()

svg = d3.select "div#inner"
    .append "svg"
    .attr "width", WIDTH
    .attr "height", HEIGHT
    .append "g"
    .attr "transform", "translate(#{WIDTH / 2}, #{HEIGHT / 2})"

angle = (d) ->
    a = (d.startAngle + d.endAngle) * 90 / Math.PI - 90
    if a > 90 then a - 180 else a

totalCount = (data) ->
    data
        .map (x) -> x.value
        .reduce ((x1, x2) -> x1 + x2), 0

makeArc = ->
    d3.svg.arc()
        .outerRadius OUTER_RADIUS
        .innerRadius INNER_RADIUS

makePie = ->
    d3.layout.pie()
        .sort null
        .value (d) -> +d.value

createArcs = (g, arc) ->
    g.append "path"
        .attr "d", arc
        .style "fill", (d, i) -> color i
        .each (d) ->
            console.log("enter on " + JSON.stringify(d));
            this._current = d.data

createText = (g, arc) ->
    g.append "text"
        .attr "transform", (d) ->
            t = "translate(#{arc.centroid d})"
            r = "rotate(#{angle d})"
            t + r
        .attr "dy", ".35em"
        .style "text-anchor", "middle"
        .text (d) -> d.data.text

transitionArcs = (data, arc) ->
    data.select "path"
        .transition()
        .delay 250
        .duration 2000
        .attrTween "d", arcTween arc

transitionText = (data, arc) ->
    data.select "text"
        .text (d) ->
            if  d.data.value > 0
                d.data.text
            else
                null
        .attr "fill-opacity", "0.0"
        .attr "transform", (d) ->
            t = "translate(#{arc.centroid d})"
            r = "rotate(#{angle d})"
            t + r
        .transition()
        .duration 500
        .delay 2250
        .attr "fill-opacity", "1.0"

arc = makeArc()

this.go = (word) ->
    d3.json "/shake/" + word, (error, json) ->
        if error
            console.warn error
        else
            if (totalCount json.result) == 0
                svg.selectAll ".arc path"
                    .transition()
                    .duration 500
                    .attr "fill-opacity", "0.0"
                svg.selectAll ".arc text"
                    .transition()
                    .duration 500
                    .attr "fill-opacity", "0.0"
            else
                svg.selectAll ".arc path"
                    .transition()
                    .duration 250
                    .attr "fill-opacity", "1.0"

                pie = makePie()

                data = svg.selectAll ".arc"
                    .data(pie json.result)

                g = data.enter()
                    .append "g"
                    .attr "class", "arc"

                createArcs g, arc
                createText g, arc

                transitionArcs data, arc
                transitionText data, arc

                data.exit().remove()

arcTween = (arc) ->
    (a) ->
        i = d3.interpolate this._current, a
        this._current = i(0)
        (t) -> arc(i t)

$("#type-in").bind 'input', ->
    text = $(this).val()
    if text == "" then text = "*BOGUS*"
    go text

autoGo = (word) ->
    $("#type-in").val word
    go word

setTimeout (->
    autoGo "love"
), 10000
