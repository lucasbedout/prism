from prism import router
from werkzeug.wrappers import Request, Response

@Request.application
def application(request):
    return Response(router.dispatch(request))

