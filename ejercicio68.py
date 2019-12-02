def get_input():
  bits = input("Bits: ")
  
  return bits
  
def division(bits):
  num = bits.count("1")
  if num % 2 == 0:
    parity = 0
  else:
    parity = 1
  
  return parity
  
def print_parity(parity):
  print("Parity bit: ", parity)
  
def main():
  bits = get_input()
  if bits != "":
    parity = division(bits)
    print_parity(parity)
  else:
    return True

while True:  
  blank_line = main()
  if blank_line == True:
    break
  
  
