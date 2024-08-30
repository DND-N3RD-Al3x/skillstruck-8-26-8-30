def days_in_month(month):
    if month == 1:
        month = 31  
    elif month == 2:
        month = 28  
    elif month == 3:
        month = 31  
    elif month == 4:
        month = 30  
    elif month == 5:
        month = 31  
    elif month == 6: 
        month = 30  
    elif month == 7:
        month = 31  
    elif month == 8:
        month = 31 
    elif month == 9:
        month = 30  
    elif month == 10:
        month = 31 
    elif month ==11:
        month = 30 
    elif month ==12:
        month = 31  

    print(month)

# Example usage:
dat = int(input())
days_in_month(dat)  
