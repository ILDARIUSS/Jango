from http.server import HTTPServer, BaseHTTPRequestHandler


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()

        with open("contacts.html", "r", encoding="utf-8") as file:
            html = file.read()

        self.wfile.write(html.encode("utf-8"))


if __name__ == "__main__":
    server = HTTPServer(("127.0.0.1", 8000), RequestHandler)
    print("Сервер запущен: http://127.0.0.1:8000")
    server.serve_forever()
