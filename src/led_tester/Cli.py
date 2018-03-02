"""Console script for LED tester"""
import sys
import click
click.disable_unicode_literals_warning = True

@click.command()
@click.option("--input", default=None, help="input URI (file or URL)")
def main(input=None):
    """Console script for LED tester"""

    print("input", input)
    N, instructions = parseFile(input)
    ledtester = LEDtester(N)

    for instruction in instructions:
        ledtester.apply(instruction)

    print('#occupied: ', ledtester.countOccupied())
    return 0

if __name__ == "__main__":
    sys.exit(main())