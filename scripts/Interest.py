def interest(principal, time, rate):
    compound_interest = principal * ( (1+rate/100)**time - 1)  
    return compound_interest
