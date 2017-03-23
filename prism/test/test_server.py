from prism import server, router

def hello(request):
  return 'hello world'

router.get('/hello', hello)

server.run()
