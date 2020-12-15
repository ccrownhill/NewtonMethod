#!/usr/bin/python3

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

def newton_root_recursion(xn, f, f_prime, margin, verbose=False):
    pass

def calculate_roots(start_values, f, f_prime, margin=1e-12, verbose=False):
    roots = list()
    for start_x in start_xs:
        print(f"Starting with x value: {start_x} ...\n")
        root = newton_root(start_x, f, f_prime, margin=margin, verbose=verbose)
        print(f"\t-->Calculated root value: {root}\n\n") 
        if root:
            roots.append(root)
    return roots

def generate_root_output(roots):

    if not roots:
        return "No roots found"

    root_output = "Roots:"
    for i in range(len(roots)):
        root_output += f"\nx{i+1} = {roots[i]}"
    return root_output


if __name__=="__main__":
    f = lambda x: x**2 + 1
    f_prime = lambda x: 2*x

    margin = 1e-12
    start_xs = [ -2, 0, 3 ]


    roots = calculate_roots(start_xs, f, f_prime, margin=margin, verbose=False)
    root_output = generate_root_output(roots) 

    print(root_output)
