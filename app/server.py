from http.server import HTTPServer, BaseHTTPRequestHandler
import socket


class SimpleHttpRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hostname: " + socket.gethostname().encode())
        print('Request: %s' % self.requestline)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hostname: " + socket.gethostname().encode())
        print('Request: %s' % self.requestline)
        print('Body: %s' % body)


SERVER_PORT = 8000
httpd = HTTPServer(('0.0.0.0', SERVER_PORT), SimpleHttpRequestHandler)
print('Listening on port %s ...' % SERVER_PORT)
httpd.serve_forever()
