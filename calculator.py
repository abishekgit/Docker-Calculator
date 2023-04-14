import click


@click.command()
@click.option('--num1', prompt='Enter the first number', type=float)
@click.option('--num2', prompt='Enter the second number', type=float)
@click.option('--op', prompt='Enter the operator (+, -, *, /)', type=click.Choice(['+', '-', '*', '/']))
def calculator(num1, num2, op):
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            click.echo("Error: cannot divide by zero")
            return
        else:
            result = num1 / num2

    click.echo(f"{num1} {op} {num2} = {result}")


if __name__ == '__main__':
    calculator()
