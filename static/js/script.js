function predict() {
  d3.json("/predict").then((data, error) => {
    if (error) throw error;
    console.log(data[2]);

    if (data[2] == "Y") {
      var weatherTomorrow = d3
        .select("#tomorrow")
        .append("h5")
        .attr("id", "prediction")
        .text(`Rain!`);

      var weatherPhoto = d3
        .select("#prediction")
        .append("img")
        .attr(
          "src",
          "https://media3.giphy.com/media/3oKIPstwMF15FghbYQ/giphy.gif?cid=ecf05e477o0xgf2sab6pate7l5q1lpehzdky2qm1q9epu5ty&rid=giphy.gif"
        )
        .attr("class", "card-img-bottom rounded my-2")
        .attr("id", "gif");
    } else if (data[2] == "N") {
      var weatherTomorrow = d3
        .select("#tomorrow")
        .append("h5")
        .attr("id", "prediction")
        .text(`No rain!`);

      var weatherPhoto = d3
        .select("#prediction")
        .append("img")
        .attr(
          "src",
          "https://media0.giphy.com/media/xTiQyjjxLwrcJjcoko/giphy.gif?cid=ecf05e47ishmcua7jmjnf7d60ln6smgnkfpp8w3rzn3gdtg1&rid=giphy.gif"
        )
        .attr("class", "card-img-bottom rounded my-2")
        .attr("id", "gif");
    }
  });
}

function updateData() {
  d3.select("tomorrow").remove();
  d3.select("#prediction").remove();
  d3.select("#gif").remove();

  predict();
}
var year_selected = d3.select("#predict");
year_selected.on("submit", updateData);
