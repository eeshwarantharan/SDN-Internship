const http = require('http');
const fs = require('fs');
const sqlite3 = require('sqlite3');
const url = require('url');
const PORT = 8080;

// Define a function to get the password and call the callback function
function getPass(query, callback) {
    let sqlQuery = `SELECT passkey FROM password WHERE passkey = '${query}'`;

    const db = new sqlite3.Database('./test.sl3', sqlite3.OPEN_READWRITE, (err) => {
        if (err) {
            console.error('Database error:', err.message);
            return callback(err, null);
        }

        db.all(sqlQuery, function (err, row) {
            if (err) {
                console.error('Database error:', err.message);
                db.close();
                callback(err, null);
            } else {
                const bool1 = [];
                if (row) {
                    for (let i = 0; i < row.length; i++) {
                        bool1[i] = row[i].passkey;
                    }
                }
                db.close();
                callback(null, bool1);
            }
        });
    });
}

// Define a function to serve HTML files
function serveHTML(filename, response) {
    fs.readFile(filename, 'utf8', (err, data) => {
        if (err) {
            response.writeHead(500, { 'Content-Type': 'text/plain' });
            response.end('Internal Server Error');
        } else {
            response.writeHead(200, { 'Content-Type': 'text/html' });
            response.end(data);
        }
    });
}

// Create an HTTP server
http.createServer((request, response) => {
    const parsedUrl = url.parse(request.url, true);

    if (parsedUrl.pathname === '/getBool1') {
        const query = parsedUrl.query.query;

        if (query) {
            getPass(query, (err, bool1) => {
                if (err) {
                    response.writeHead(500, { 'Content-Type': 'text/plain' });
                    response.end('Internal Server Error');
                } else {
                    response.writeHead(200, { 'Content-Type': 'application/json' });
                    response.end(JSON.stringify({ bool1 }));
                }
            });
        } else {
            response.writeHead(400, { 'Content-Type': 'text/plain' });
            response.end('Query parameter "query" is missing in the URL.');
        }
    } else if (parsedUrl.pathname === '/MainPage.html') {
        serveHTML('./MainPage.html', response);
    } else if (parsedUrl.pathname === '/success.html') {
        serveHTML('./success.html', response);
    } else if (parsedUrl.pathname === '/MainPage_Query.html') {
        serveHTML('./MainPage_Query.html', response);
    } else {
        response.writeHead(404, { 'Content-Type': 'text/plain' });
        response.end('Not Found');
    }
}).listen(PORT);