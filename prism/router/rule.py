from werkzeug.routing import Rule

class RouterRule(Rule):

    def __init__(self, view, *args, **kwargs):
        self.view = view
        super(RouterRule, self).__init__(*args, **kwargs)

    def empty(self):
        """We need this method if we want to use
           Submounts or Subdomain factories
        """
        defaults = dict(self.defaults) if self.defaults else None
        return RouterRule(self.view, self.rule, defaults, self.subdomain,
                        self.methods, self.build_only, self.endpoint,
                        self.strict_slashes, self.redirect_to,
                        self.alias, self.host)
