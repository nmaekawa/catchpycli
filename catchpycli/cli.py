"""
catchpycli.cli
--------------
command line interface for catchpy api client
"""



import click


@click.command()
def main(args=None):
    """Console script for catchpycli"""
    click.echo("Replace this message by putting your code into "
               "catchpycli.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")


if __name__ == "__main__":
    main()
