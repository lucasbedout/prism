from werkzeug.routing import Map
from prism.router.rule import RouterRule

class Router:

    routes = []

    routes_map = None

    def get(self, route, callable):
        self.add_route(route, 'GET', callable)

    def post(self, route, callable):
        self.add_route(route, 'POST', callable)

    def put(self, route, callable):
        self.add_route(route, 'PUT', callable)

    def patch(self, route, callable):
        self.add_route(route, 'PATCH', callable)

    def delete(self, route, callable):
        self.add_route(route, 'DELETE', callable)

    def add_route(self, route, method, callable):
        rule = RouterRule(callable, route, methods=[method], endpoint=route)
        self.routes.append(rule)

    def get_map(self):
        if not self.routes_map:
            self.routes_map = Map(self.routes)
        return self.routes_map

    def dispatch(self, request):
        urls = self.get_map().bind_to_environ(request.environ)
        rule, arguments = urls.match(return_rule=True)
        return rule.view(request)

router = Router()


