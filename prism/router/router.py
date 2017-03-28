from werkzeug.routing import Map
from prism.router.rule import RouterRule

class Router:

    def __init__(self):
        self.routes = []
        self.routes_map = None

    def get(self, route, callable):
        return self.add_route(route, 'GET', callable)

    def post(self, route, callable):
        return self.add_route(route, 'POST', callable)

    def put(self, route, callable):
        return self.add_route(route, 'PUT', callable)

    def patch(self, route, callable):
        return self.add_route(route, 'PATCH', callable)

    def delete(self, route, callable):
        return self.add_route(route, 'DELETE', callable)

    def add_route(self, route, method, callable):
        rule = RouterRule(callable, route, methods=[method], endpoint=route)
        self.routes.append(rule)
        return rule

    def get_map(self):
        '''
        Get the route map
        '''
        if not self.routes_map:
            self.routes_map = Map(self.routes)
        return self.routes_map

    def dispatch(self, request):
        '''
        Main router method, dispatch a call to the right view
        and handle the middleware
        '''
        urls = self.get_map().bind_to_environ(request.environ)
        rule, args = urls.match(return_rule=True)

        if rule.middle(request):
            return rule.view(request, **args)
        return 'Error'

router = Router()


