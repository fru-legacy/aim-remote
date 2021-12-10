import click
import asyncio
from server import up

@click.group()
def cli():
    pass

@cli.command('up')
@click.option('-h', '--host', default='0.0.0.0', type=str)
@click.option('-p', '--port', default=4902, type=int)
def up_command(host, port):
    asyncio.run(up(host, port))

if __name__ == '__main__':
   cli()