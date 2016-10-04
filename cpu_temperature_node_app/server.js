var express = require('express');
var redis = require('redis');
const path = require('path');

var client = redis.createClient(6379, "redis" );
var app = express();

app.get('/temperature', function (req, res) {
  client.get("currentCPUTemperature", (err,value)=>res.send(value))
});

app.get('/', function(req, res){
  res.sendFile(path.join(__dirname, "index.htm"))
})

app.listen(3000);
