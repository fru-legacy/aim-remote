import click

@click.group()
def cli():
    pass

@cli.command('up')
@click.option('-h', '--host', default='0.0.0.0', type=str)
@click.option('-p', '--port', default=4902, type=int)
def my_list_command(host, port):
    print(host)
    print(port)

if __name__ == '__main__':
   cli()