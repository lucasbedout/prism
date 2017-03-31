import click

@click.group()
def cli():
    pass

@click.command()
@click.option('-h', '--host', default='0.0.0.0', help='Host the server will run on')
@click.option('-p', '--port', default=5555, help='Port the server will run on')
def run(host, port):
    from .app.kernel import application
    from prism import server
    server.run(application, host, port)
    click.echo('Server started on port http://{}:{}'.format(host, port))

@click.command()
def routes():
    from .app.kernel import router
    from tabulate import tabulate
    routes = [[r.endpoint, r.view.__name__] for r in router.routes]
    click.echo(tabulate(routes, headers=['Endpoint', 'Method'], tablefmt='orgtbl'))

cli.add_command(run)
cli.add_command(routes)

if __name__ == '__main__':
    cli()
