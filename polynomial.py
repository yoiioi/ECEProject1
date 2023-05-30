###############################
# Team members- Please enter your names here
# Name1: Katherine Gayeon Kim
# Name2: Carly Rosenstrauch
###############################


def display_menu():
    """Display the list of polynomial available tools"""
    print("1-Insert; 2-Remove; 3-Info; 4-Evaluate; 5-Scaling; 6-Derive; 7-Integrate")
    print("8-Summation; 9-Subtract; 10-Multiply; 11-Divide")

def display_list(list_poly):
    for i in range (len(list_poly)):
        print(str(i+1)+":",get_expression(list_poly[i]))

def get_polynomial():
    degree = int(input("Degree of polynomial? "))
    coefficients = []
    for i in range(degree + 1):
        coefficient = float(input(f"Enter coefficient of x^{i}: "))
        coefficients = coefficients + [coefficient]
    return coefficients

def get_expression(poly):
    polynomial = ""
    i = 0
    if all(coeff == 0 for coeff in poly):
        return "0.0"
    for i in range(len(poly)):
        if poly[i] != 0:
            if i == 0:
                polynomial += str(poly[i])
            elif i == 1:
                if poly[i] < 0:
                    polynomial += "-" + str(abs(poly[i])) + "x"
                else:
                    polynomial += "+" + str(poly[i]) + "x"
            else:
                if poly[i] < 0:
                    polynomial += "-" + str(abs(poly[i])) + "x^" + str(i)
                else:
                    polynomial += "+" + str(poly[i]) + "x^" + str(i)
    return polynomial

def info(poly):
    degree = len(poly) - 1
    if poly[degree] == 0.0:
        degree = degree-1
    even = all(poly[i] == 0.0 for i in range(1, degree+1, 2))
    odd = all(poly[i] == 0.0 for i in range(0, degree+1, 2))
    if even and odd:
        parity = "zero polynomial"
    elif even:
        parity = "even"
    elif odd:
        parity = "odd"
    else:
        parity = "neither odd nor even polynomial"
    return f"Degree is {degree} and it is {parity}"

def evaluate(poly, x):
    result = 0
    for i in range(len(poly)):
        result += poly[i] * x**(i)
    return result

def scale(poly,x):
    for i in range(len(poly)):
        if x != 0:
            poly[i] = poly[i]*x
        else:
            poly[i] = 0.0
    return poly

def derive(dpdx):
    if len(dpdx) <= 1:
        return [0.0]
    poly = dpdx[1:]
    for i in range(len(poly)):
        poly[i] = poly[i] * (i+1)
    return poly

def integrate(poly, lo, up):
    antiderivative = [0] * (len(poly) + 1)
    for i in range(len(poly)):
        antiderivative[i+1] = poly[i] / (i+1)
    integral = evaluate(antiderivative, up) - evaluate(antiderivative, lo)
    return integral

def integrate(poly, lo, up):
    integral = [0.0] * (len(poly) + 1)
    integral[0] = 0.0
    for i in range(len(poly)):
        integral[i+1] = poly[i] / (i+1)
    lower_bound = 0.0
    for i in range(len(integral)):
        lower_bound += integral[i] * (lo ** i)
    upper_bound = 0.0
    for i in range(len(integral)):
        upper_bound += integral[i] * (up ** i)
    return upper_bound - lower_bound

def add(p1, p2):
    max_size = max(len(p1), len(p2))
    p = [0.0] * max_size
    min_size = min(len(p1), len(p2))
    for i in range(min_size):
        p[i] = p1[i] + p2[i]
    if len(p1) > len(p2):
        for i in range(min_size, max_size):
            p[i] = p1[i]
    elif len(p1) < len(p2):
        for i in range(min_size, max_size):
            p[i] = p2[i]
    while len(p) > 1 and p[-1] == 0.0:
        del p[-1]
    return p

def subtract(p1, p2):
    p3 = [-coef for coef in p2]
    return add(p1, p3)

def multiply(p1, p2):
    p = [0.0]
    for i in range(len(p1)):
        p3 = [p1[i] * x for x in p2]
        p3 = [0.0] * i + p3
        p = add(p, p3)
    return p