import matplotlib.pyplot as plt
import numpy as np

# Read x values from the file
with open('DSAxval.txt', 'r') as file:
    x_values = [int(line.strip()) for line in file.readlines()]

# Define the expressions as functions
def expression_1(x):
    return x**2 + 7*x + 2

def expression_2(x):
    return 3*x + 2

def expression_3(x):
    return x**2

def expression_4(x):
    return x**3

def expression_5(x):
    return x**5

def expression_6(x):
    return x**3 + 2*x**2 + x + 10

def expression_7(x):
    return x**4 - 3*x**3 + 2*x**2 - x + 11

def expression_8(x):
    return np.sin(x)

def expression_9(x):
    return np.cos(x)

def expression_10(x):
    return x**5 + 4*x**4 + x**3 - 2*x**2 + 100

# Store all expressions in a dictionary with their descriptions
expressions_dict = {
    '1': (expression_1, 'x^2 + 7x + 2'),
    '2': (expression_2, '3x + 2'),
    '3': (expression_3, 'x^2'),
    '4': (expression_4, 'x^3'),
    '5': (expression_5, 'x^5'),
    '6': (expression_6, 'x^3 + 2x^2 + x + 10'),
    '7': (expression_7, 'x^4 - 3x^3 + 2x^2 - x + 11'),
    '8': (expression_8, 'sin(x)'),
    '9': (expression_9, 'cos(x)'),
    '10': (expression_10, 'x^5 + 4x^4 + x^3 - 2x^2 + 100')
}

# Generate answers for all expressions
answers = [[expr(x) for x in x_values] for expr, _ in expressions_dict.values()]

# Plot a single expression
def plot_expression(expression, x_values, color, label):
    plt.plot(x_values, expression, color=color, label=label)

# Plot all expressions
def plot_all(expressions, x_values, colors):
    for i, (expr, color) in enumerate(zip(expressions, colors), start=1):
        plot_expression(expr, x_values, color, f'Expression {i}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    print("Choose the expressions you want to plot (separate with commas), or type 'all' to plot all expressions:")
    for i, (_, desc) in expressions_dict.items():
        print(f"{i}. {desc}")

    user_input = input("Your choice: ")  # Read user input using input()

    selected_expressions = []  # List to store selected expressions for writing to output file

    if user_input.lower() == 'all':
        colors = plt.cm.jet(np.linspace(0, 1, len(expressions_dict)))  # Generate a range of colors
        plot_all(answers, x_values, colors)
        selected_expressions = expressions_dict.values()
    else:
        choices = [choice.strip() for choice in user_input.split(',')]
        for choice in choices:
            expr_info = expressions_dict.get(choice)
            if expr_info:
                plot_expression(answers[int(choice) - 1], x_values, 'b', f'Expression {choice}')
                selected_expressions.append(expr_info)
            else:
                print(f"Invalid choice: {choice}")
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.grid(True)
        plt.show()

    # Write the results of selected expressions to the output file
    with open('output.txt', 'a') as output_file:
        output_file.write("Results:\n")
        for i, (expr, desc) in enumerate(selected_expressions, start=1):
            output_file.write(f"Expression {i}: {desc}\n")
            output_file.write(f"Results for {desc}:\n")
            output_file.write(f"{', '.join(map(str, [expr(x) for x in x_values]))}\n")
            output_file.write("\n")

if __name__ == "__main__":
    main()
