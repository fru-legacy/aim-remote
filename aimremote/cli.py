import click
import asyncio
from aimremote.server import up

@click.group()
def cli():
    pass

@cli.command('up')
@click.option('-h', '--host', default='0.0.0.0', type=str)
@click.option('-p', '--port', default=4902, type=int)
@click.option('-t', '--security-token', type=str, required=True)
def up_command(host, port, security_token):
    print(security_token)
    asyncio.run(up(host, port))

if __name__ == '__main__':
   cli()