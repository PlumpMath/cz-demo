# -*- coffee-tab-width: 4; -*-

svg = d3.select "div#inner"
    .append "svg"
    .attr "width", 600
    .attr "height", 600

rgb_str = (d) ->
    rgbs = d.rgb.map (v) -> (v * 255).toFixed()
    "rgb(#{rgbs.join()})"

counter = 0

oneCycle = (path) ->
    d3.json path + "/" + counter, (error, json) ->
        if error
            console.warn error
        else
            circle = svg.selectAll "circle"
            c = circle.data json.result, (d) -> +d.key

            c.transition()
                .duration 1000
                .ease "elastic"
                .attr "cx", (d) -> d.x * 600
                .attr "cy", (d) -> d.y * 600
                .attr "r", (d) -> d.r * 40
                .attr "fill", rgb_str

            c.enter()
                .append "circle"
                .attr "cx", (d) -> d.x * 600
                .attr "cy", (d) -> d.y * 600
                .attr "r", 0
                .transition()
                .duration 1000
                .attr "r", (d) -> d.r * 40
                .attr "fill", rgb_str

            c.exit()
                .transition()
                .duration 1000
                .attr "r", 0
                .remove()

            counter = counter + 1

this.go = (path) ->
    setInterval (-> oneCycle path), 3000
    oneCycle path
