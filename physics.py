
def main():
    """
    """
    input_file = open('values.csv', 'r', encoding="utf-8")

    for line in input_file:
        value = line.split(',')
        result = equation(value[0], value[1], value[2])
        write_result(result)

        

def equation(a, b ,c):
    """Insert physics equation here
    """
    return #equation result


def write_result(result):
    """Write to the output file with the result of the equation
    """
    #open file
    with open('results.csv', 'a', encoding="utf-8") as f:
        f.write( str(result) + ',' )