console.log("------------------------------");
console.log("AIHI - Weather.js");
console.log("------------------------------");

//----------------------------------------
// Importing modules
//----------------------------------------
var express = require("express");
var app = express();
const bodyParser = require("body-parser");
var dateFormat = require('dateformat');

//------------------------------------------------------
// configuration
//------------------------------------------------------
const hostname = 'localhost';
const port = 3000;

// ACTION: include your own API Key
const apikey = "0d696bd7c821447dc21fa638a5f6344f";

//------------------------------------------------------
// standard functions
//------------------------------------------------------
/*
  prints useful debugging information about an endpoint we are going to service

  @param urlPattern
    url pattern

  @param req
    request object

  @return
    true/false
 */
function printDebugInfo(urlPattern, req) {
  console.log();
  console.log("-----------[ Debug Info ]------------");

  console.log(`Servicing ${urlPattern} ..`);
  console.log("Servicing " + req.url + " ..");

  console.log("> req.params:" + JSON.stringify(req.params));
  console.log("> req.body:" + JSON.stringify(req.body));

  console.log("--------[ Debug Info Ends ]----------");
  console.log();
}

//------------------------------------------------------
// handler functions
//------------------------------------------------------
function getWeather(req, res) {
  var request = require('request');

  var targetCity = req.body.queryResult.parameters['city'].toLowerCase();
  console.log("city " + targetCity);

  // if a city cannot be found, set a default
  if (targetCity == null) {
    targetCity = "singapore";
  }

  var targetDate = req.body.queryResult.parameters['date'];

  // var month = req.params.month.padStart(2, "0");
  // var day = req.params.day.padStart(2, "0");

  var targetFormattedYear = dateFormat(targetDate, "yyyy");
  console.log("year: " + targetFormattedYear);

  var targetFormattedMonth = dateFormat(targetDate, "mm");
  console.log("month: " + targetFormattedMonth);

  var targetFormattedDay = dateFormat(targetDate, "dd");
  console.log("day: " + targetFormattedDay);


  // res.status(200).send("test");
  // return;

  var url = `http://api.openweathermap.org/data/2.5/forecast?q=${targetCity}&apikey=${apikey}`;
  console.log(url);

  request(url, function(error, response, body) {
    if (error) {
      // Print the error if one occurred
      console.log('error:', error);

      res.status(500).send("some error");
    } else {

      // Print the response status code if a response was received
      console.log('statusCode:', response && response.statusCode);

      // Print the HTML for the Google homepage.
      console.log('body:', body);

      var data = JSON.parse(body);

      // res.status(200).send(data);
      // return;

      console.log("total length: " + data.list.length);

      var result = "none found";

      for (var i = 0; i < data.list.length; i++) {
        var currentWeather = data.list[i];
        var currentDateObj = new Date(currentWeather.dt * 1000);
        var currentWeatherDesc = currentWeather.weather[0].description;
        var currentDate = currentWeather.dt_txt;

        var currentFormattedYear = dateFormat(currentDateObj, "yyyy");
        console.log("Current Year: " + currentFormattedYear);

        var currentFormattedMonth = dateFormat(currentDateObj, "mm");
        console.log("Current Month: " + currentFormattedMonth);

        var currentFormattedDay = dateFormat(currentDateObj, "dd");
        console.log("Current Day: " + currentFormattedDay);

        if (
          targetFormattedYear == currentFormattedYear &&
          targetFormattedMonth == currentFormattedMonth &&
          targetFormattedDay == currentFormattedDay
        ) {
          // once we found our correct date, we can stop the loop
          result = `Weather found at ${currentDate} is ${currentWeatherDesc}`;

          // with this break
          break;
        }
      }

      // here, this is the correct place to send the response
      var dialogFlow_output = {
        fulfillmentText: result
      };

      res.send(dialogFlow_output);
    }
  });
}

//--------------------------------------------
// Middleware functions
//--------------------------------------------
var urlencodedParser = bodyParser.urlencoded({ extended: false });
var jsonParser = bodyParser.json();

//------------------------------------------------------
// MF configuration
//------------------------------------------------------
app.use(urlencodedParser);
app.use(jsonParser);

//----------------------------------------
// Endpoints
//----------------------------------------
// GET >> http://localhost:3000/
app.get("/", function(req, res) {
  printDebugInfo("/", req);

  res.send('<h1>This is my weather web app!!!! =(((( </h1>');
});

// POST >> http://localhost:3000/chat
app.post("/chat", function(req, res) {
  printDebugInfo("/chat", req);

  // let's get the intent name
  var intent = req.body.queryResult.intent.displayName;

  // you can get the intent name from your
  // DialogFlow > Diagnostic Info > Fulfillment Request >
  // queryResult > intent > displayName
  switch (intent) {
    case "getWeatherIntent":
      getWeather(req, res);

      break;
  }
});

//----------------------------------------
// Main
//----------------------------------------
var listener = app.listen(process.env.PORT || 3000, process.env.IP, () => {
  var actual_hostname = process.env.IP;
  var actual_port = listener.address().port;
  console.log(`Server started and accessible via http://${actual_hostname}:${actual_port}/`);
});