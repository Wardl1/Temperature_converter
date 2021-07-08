""" Converting Fahrenheit to Celsius v1
Converting from degrees Fahrenheit to Celsius
Function takes in a value, does the conversion and puts the answer into a list
"""


def to_c(from_f):
    celsius = (from_f - 32) * 5/9
    return celsius


# Main Routine
temperatures = [0, 32, 100]
converted = []

for item in temperatures:
    answer = to_c(item)
    ans_statement = "{} degrees F is {} degrees C".format(item, answer)
    converted.append(ans_statement)

for i in converted:
    print(i)
