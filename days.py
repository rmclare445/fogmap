days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def day_of_year(year, month, day):
    
    dim = days_in_month
    if year%4 == 0:
        dim[1] = 29 
        
    if month > 1:
        predays = sum(dim[:month-1])
    else:
        predays = 0
        
    return predays + day

#print(day_of_year(2021,8,15))