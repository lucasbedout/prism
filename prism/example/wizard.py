import click
from .app.kernel import application
from prism import server

@click.group()
def cli():
    pass

@click.command()
def run():
    server.run(application, '0.0.0.0', 5555)
    click.echo('Server started on port http://0.0.0.0:5555')

cli.add_command(run)

if __name__ == '__main__':
    cli()
