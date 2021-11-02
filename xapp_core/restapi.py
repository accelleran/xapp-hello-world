import tornado.ioloop
import tornado.web

class MainApiHandler(tornado.web.RequestHandler):
    def initialize(self, in_queue):
        self.in_queue = in_queue
    def get(self):
        self.write("Write a message into the in_queue...\n")
        self.in_queue.put("Message from restapi main handler")
        self.write("Message written.\n")

class ActionsHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.write("init action handler\n")
    def get(self):
        self.write("action handler get\n")

class RequestHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.write("init request handler\n")
    def get(self):
        self.write("request handler get\n")
    def post(self):
        self.set_header("Content-Type", "text/plain")
        self.write("You wrote " + self.get_body_argument("message"))

def run(settings, in_queue):
    app = tornado.web.Application([
        ("/api/", MainApiHandler, {"in_queue":in_queue}),
        ("/api/actions", ActionsHandler),
        ("/api/request", RequestHandler),
    ], debug=True)
    app.listen(8888, "0.0.0.0")
    tornado.ioloop.IOLoop.current().start()

