#PiApproximation.py

"""This program prompts the user for an error tolerence called error. It will
find the minimum number of terms required to get an approximation of pi"""
      
pi = 3.14159265358979

print("We are finding the minimum number of terms needed to get an approximation" + 
      " of pi accurate within our error tolerance.\n")

error = float(input("Input error tolerance: "))

print("\nNumber of Terms\t\tPi Approximation")

terms = 1
current_pi = 0.0
denominator = 1
sign = 1

current_error = 100.0

while current_error > error:
    term_val = 4.0 / denominator
    
    if sign == 1:
        current_pi = current_pi + term_val
        sign = -1
    elif sign == -1:
        current_pi = current_pi - term_val
        sign = 1
        
    print(terms, "\t\t\t", format(current_pi, ".6f"))
    
    current_error = abs(pi - current_pi)
    
    if current_error > error:
        terms = terms + 1
        denominator = denominator + 2

print("\nAfter", terms, "terms, pi is approximately", format(current_pi, ".6f") + ".")
print("Our error is", format(current_error, ".6f"), "which is less than or equal to", format(error, ".6f") + ".")
