var net = require('net');

const port = 2802;

var server = net.createServer(function(conn) {
    console.log('connected');

    conn.on('data', function (data) {
        console.log(data + ' from ' + conn.remoteAddress + ' ' +
            conn.remotePort);
        conn.write('Repeating: ' + data);
    });

    conn.on('close', function() {
        console.log('client closed connection');
    });

}).listen(port);

server.on('listening', function() {
    console.log(`Server listening on port:${port}/`);
});

server.on('error', function(err){
    if (err.code == 'EADDRINUSE') {
        console.warn('Address in use, retrying...');

        setTimeout(() => {
            server.close();
            server.listen(PORT);
        }, 1000);

    } else {
        console.error(err);
    }
});

