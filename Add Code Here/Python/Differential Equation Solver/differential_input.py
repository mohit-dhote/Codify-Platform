import random
import math

def euler_method(func, initial_condition, x_range, step_size):
    x_start, x_end = x_range
    x_values = []
    y_values = []

    x = x_start
    y = initial_condition

    while x <= x_end:
        x_values.append(x)
        y_values.append(y)

        # Update y using Euler's method
        y += step_size * func(x, y)

        x += step_size

    return x_values, y_values

def diff_input():
    # ... (Your input code for the ODE and initial conditions)

if __name__ == '__main__':
    funcs, init_conditions, x_range, n = diff_input()
    
    # Ensure that you have the appropriate functions and initial conditions
    if len(funcs) != 1 or len(init_conditions) != 1:
        print("Please provide a single first-order ODE and initial conditions.")
    else:
        func = lambda x, y: eval(funcs[0])  # Convert the user-provided function to a Python function
        x_values, y_values = euler_method(func, init_conditions[0], x_range, step_size=0.1)  # Adjust step_size as needed
        print("Solved ODE values:")
        for x, y in zip(x_values, y_values):
            print(f"x: {x}, y: {y}")
