var express = require('express');
var port = 3000;
var app = express();

app.use('/info', function(req, res, next) {
      console.log('info request received')
      next();
    });

app.get('/info/data', function(req, res) {
  console.log('\tsending data on ' + new Date().toUTCString())
//  console.log('\tsending data on ' + new Date().toJSON())
  res.send('{ "data": "health state", "status": 111 }')
});

app.listen(port);
console.log('');
console.log('Listening on port ' + port);
console.log('');

module.exports.getApp = app;
