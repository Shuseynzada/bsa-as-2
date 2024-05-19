from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

class MyHttpRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'index.html'
        return SimpleHTTPRequestHandler.do_GET(self)

# Set the directory where the server will look for files
web_dir = os.path.join(os.path.dirname(__file__), 'web')
os.chdir(web_dir)

# Server settings
port = 8000
server_address = ('', port)

# Initialize and start the server
httpd = HTTPServer(server_address, MyHttpRequestHandler)
print(f"Serving HTTP on port http://localhost:{port}...")
httpd.serve_forever()
