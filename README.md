# Newton Method Python implementation

This short script finds the roots of a function given the function and its derivative using the [Newton Method](https://en.wikipedia.org/wiki/Newton's_method).

The Newton Method requires some starting guesses for roots which are by default `-2.0`, `-0.2`, `0.2` and `2.0`.
You can also change these manually.
Note that it is important that you choose at least as many starting values as the number of roots of the function.

## Usage

Usage output from `./newton_method -h` (see examples [here](#examples)):

```
usage: newton_method.py [-h] -f FUNCTION -d DERIVATIVE [-m MARGIN] [-p PRECISION] [start_values ...]

positional arguments:
  start_values

optional arguments:
  -h, --help            show this help message and exit
  -f FUNCTION, --function FUNCTION
  -d DERIVATIVE, --derivative DERIVATIVE
  -m MARGIN, --margin MARGIN
  -p PRECISION, --precision PRECISION
```

## Examples

To get the roots of the function `f(x) = x**2 - 1` you would issue the following command:

```
$ ./newton_method.py -f "x**2-1" -d "2*x"
Setting precision to 10 decimals (use -p or --precision to change this)

Starting with x value: -2.0 ...
	--> Calculated root value: -1.000000000000001

Starting with x value: -0.2 ...
	--> Calculated root value: -1.0

Starting with x value: 0.2 ...
	--> Calculated root value: 1.0

Starting with x value: 2.0 ...
	--> Calculated root value: 1.000000000000001

Roots:
x1 = -1.0000000000
x2 = 1.0000000000
```

Here you can specify the precision of decimal digits using `-p`:

```
$ ./newton_method.py -f "x**2-1" -d "2*x" -p 3
Setting precision to 3 decimals (use -p or --precision to change this)

Starting with x value: -2.0 ...
	--> Calculated root value: -1.000000000000001

Starting with x value: -0.2 ...
	--> Calculated root value: -1.0

Starting with x value: 0.2 ...
	--> Calculated root value: 1.0

Starting with x value: 2.0 ...
	--> Calculated root value: 1.000000000000001

Roots:
x1 = -1.000
x2 = 1.000
```

Another thing you can do is choose your own initial root guesses by appending them to the command.
The following would use `1` and `-1`:

```
$ ./newton_method.py -f "x**2-1" -d "2*x" -p "3" 1 -1
Setting precision to 3 decimals (use -p or --precision to change this)

Starting with x value: 1.0 ...
	--> Calculated root value: 1.0

Starting with x value: -1.0 ...
	--> Calculated root value: -1.0

Roots:
x1 = 1.000
x2 = -1.000
```
