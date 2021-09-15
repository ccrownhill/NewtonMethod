#!/usr/bin/python3

import argparse

def newton_root(xn, f, f_prime, margin, verbose=False):
    i = 0
    while f(xn) > margin or f(xn) < -margin:
        i += 1
        try:
            xn = xn - f(xn)/f_prime(xn)
        except ZeroDivisionError:
            print(f"Bad x-value: Derivative will become 0. You can't divide by zero.")
            return
        if verbose:
            print(f"xn in Iteration {i} = {xn}")

        if i > 1e5:
            return
    return xn

def calculate_roots(start_values, f, f_prime, margin=1e-12, verbose=False):
    roots = list()
    for start_x in start_values:
        print(f"Starting with x value: {start_x} ...")
        root = newton_root(start_x, f, f_prime, margin=margin, verbose=verbose)
        print(f"\t--> Calculated root value: {root}\n") 
        if root:
            roots.append(root)
    return roots

def remove_duplicates(roots):
    for i in range(len(roots)-1, -1, -1): # iterate backwards to prevent element skipping after deletion
        if roots.index(roots[i]) != i:
            del roots[i]
    return roots

def generate_root_output(roots, precision):

    if not roots:
        return "No roots found"

    root_output = "Roots:\n"
    for i in range(len(roots)):
        root_output += f"x{i+1} = {roots[i]:.{precision}f}\n"
    return root_output


if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--function', type=str, required=True)
    parser.add_argument('-d', '--derivative', type=str, required=True)
    parser.add_argument('-m', '--margin', type=float, default=1e-12, required=False)
    parser.add_argument('-p', '--precision', type=int, default=10, required=False)
    parser.add_argument('start_values', type=float, nargs='*', default=[-2.0, -0.2, 0.2, 2.0])
    args = parser.parse_args()

    f = lambda x: eval(args.function)
    f_prime = lambda x: eval(args.derivative)

    print(f"Setting precision to {args.precision} decimals (use -p or --precision to change this)\n")

    roots = calculate_roots(args.start_values, f, f_prime, margin=args.margin, verbose=False)

    roots = list(map(lambda x: round(x, args.precision), roots))

    roots = remove_duplicates(roots)
    root_output = generate_root_output(roots, args.precision)

    print(root_output, end='') # don't put another newline at the end
