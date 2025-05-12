# orbital_period_function.py

def orbital_period(a):
    ''' Inputs: the semi-major axis (a)
        Outputs: Orbital Period (T) '''
    T = (a**3)**(1/2) # assigning T based on the formula provided
    return T