from prism import Request, router
from werkzeug.wrappers import Response

@Request.application
def application(request):
    return Response(router.dispatch(request))

