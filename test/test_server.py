from prism import server, router

def hello(request, name):
  return 'Hello ' + name

def auth(request):
  return request.has('auth')

router.get('/', lambda request: 'Welcome!')
router.get('/hello/<name>', hello).via(auth)

server.run()
