""" Converting Celsius to Fahrenheit v1
Converting from degrees Celsuis to Fahrenheit
Function takes in a value, does the conversion and puts the answer into a list
"""


def to_f(from_c):
    fahrenheit = (from_c * 9 / 5) + 32
    return fahrenheit


# Main Routine
temperatures = [0, 40, 100]
converted = []

for item in temperatures:
    answer = to_f(item)
    ans_statement = "{} degrees c is {} degrees F".format(item, answer)
    converted.append(ans_statement)

for i in converted:
    print(i)
