var app = require('http').createServer(handler),
    io = require('socket.io').listen(app),
    fs = require('fs'),

    serialport = require("serialport"),
    SerialPort = serialport.SerialPort,
    serial = new SerialPort("/dev/ttyUSB0", {
        baudrate: 115200,
        parser: serialport.parsers.readline("\n")
    });

// ports 8000 - 9000 are open on amazon server use 8990
app.listen(8990);
console.log("Listening on port 8990");


function handler (req, res) {
    console.log("handle")
    //console.log(req)
    fs.readFile(__dirname + '/index.html',
        function (err, data) {
            if (err) {
                res.writeHead(500);
                return res.end('An Error loading index.html');
            }
            res.writeHead(200);
            res.end(data);
        });
}

io.sockets.on('connection', function (socket) {
    console.log("got data");
    socket.emit('news', { hello: 'world' });
    socket.emit('command', { hello: 'world' });
    socket.on('my other event', function (data) {
        console.log(data);
    });
});

// TODO add on disconnet
// TODO impliment protocalls

\
serial.on("data", function (data) {
    console.log("from arduino: "+data);
});
