from tg import expose, TGController , AppConfig
from wsgiref.simple_server import make_server

class HelloWorldController(TGController):

    @expose('helloworld.xhtml')
    def index(self):
        return dict(message="Hello, World!")
    
if __name__ == '__main__':
    config = AppConfig(minimal=True, root_controller = HelloWorldController())
    config.renderers.append('kajiki')
    app = config.make_wsgi_app()
    server = make_server('', 8080, app)
    server.serve_forever()
