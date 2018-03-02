"""Console script for LED tester"""
import sys
import click
click.disable_unicode_literals_warning = True

@click.command()
@click.option("--input", default=None, help="input URI (file or URL)")
def main(input=None):
    """Console script for LED tester"""
    click.echo()
    print("input", input)
    return 0

if __name__ == "__main__":
    sys.exit(main())