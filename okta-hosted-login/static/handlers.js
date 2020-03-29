
onAddRequest = function () {
    d3.select("#new_request_form")
        .classed("hidden", false)
}

onSubmitRequest = function () {
    let bub = d3.select("#address");

    console.log(bub.node().value);
}

