def decimalToBinary(n):  
    return bin(n).replace("0b", "")  
    
# Driver code  
if __name__ == '__main__':  
    print(decimalToBinary(9))  
    print(decimalToBinary(18))  
    print(decimalToBinary(7))  

