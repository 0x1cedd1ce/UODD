from http.server import SimpleHTTPRequestHandler, HTTPServer
import mimetypes

class RequestHandler(SimpleHTTPRequestHandler):
    def __intit__(self, *args, **kwargs):
        super().__init__(*args, directory="./", **kwargs)

    if not mimetypes.inited:
        mimetypes.init()
    extensions_map = mimetypes.types_map.copy()
    extensions_map.update({'.py': 'text/plain'})

handler_class = RequestHandler
httpd = HTTPServer(('', 8000), handler_class)

httpd.serve_forever()