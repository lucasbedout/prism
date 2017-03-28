from werkzeug.routing import Rule

class RouterRule(Rule):

    def __init__(self, view, *args, **kwargs):
        self.view = view
        super(RouterRule, self).__init__(*args, **kwargs)
        self.middlewares = []

    def empty(self):
        """
        We need this method if we want to use
        Submounts or Subdomain factories
        """
        defaults = dict(self.defaults) if self.defaults else None
        return RouterRule(self.view, self.rule, defaults, self.subdomain,
                          self.methods, self.build_only, self.endpoint,
                          self.strict_slashes, self.redirect_to,
                          self.alias, self.host)

    def via(self, middlewares):
        '''
        Add a middleware to the route
        '''
        if isinstance(middlewares, list):
            self.middlewares += middlewares
        else:
            self.middlewares.append(middlewares)

    def middle(self, request):
        '''
        Call the middlewares and stops the request if something is wrong
        '''
        for middleware in self.middlewares:
            if middleware(request) is False:
                return False
        return True
