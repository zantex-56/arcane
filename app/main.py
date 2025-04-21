import click
import ct
@click.group()
def cli():
    """
    Command line interface for managing CT instances.
    """
    pass

@cli.command()
@click.argument('system', type=click.Choice(['noble', 'bookworm', 'jammy', 'focal', 'buster', 'bullseye', 'sid']))
@click.argument('name', type=str)
@click.option('--path', type=str, default=None, help='The path to create the CT in. If not specified, the CT will be created in the current directory.')
def create(system, name, path):
    """
    Create a new CT instance.
    """
    ct.create_ct_base(system, name, path)

if __name__ == '__main__':
    cli()   