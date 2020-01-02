# String Formatting
def print_formatted(number):
    width = len(bin(number)[2:])
    for i in range(1, number + 1):
        dec = str(i)
        octal = oct(i)[2:]
        hexa = hex(i)[2:].upper()
        binary = bin(i)[2:]
        print(f"{dec:>{width}} {octal:>{width}} {hexa:>{width}} {binary:>{width}}")

# String Validators
s = input()
print(any(c.isalnum() for c in s))
print(any(c.isalpha() for c in s))
print(any(c.isdigit() for c in s))
print(any(c.islower() for c in s))
print(any(c.isupper() for c in s))
