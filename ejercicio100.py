from ejercicio57 import ano_bisi as ano

def days_in_month(month, year): 
    days_31 = [1,3,5,7,8,10,12]
    days_30 = [4,6,9,11]
    feb = 2
    
    if month in days_31: 
        print("Este mes tiene 31 días")
    elif month in days_30: 
        print("Este mes tiene 30 días")
    elif month == feb: 
        if ano(year): 
            print("Este mes tiene 29 días")
        else: 
            print("Este mes tiene 28 días")
          
    
