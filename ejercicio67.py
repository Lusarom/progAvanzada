def take_input():
  age_list = []
  age = "A"
  while True:
    age = input("What is the age? ")
    if age == "":
      break
    age_list.append(int(age))
  return age_list
  
def age_values(age_list):
  index = 0
  cost_list = []
  for x in range(len(age_list)):
    if age_list[index] <= 2:
      cost_list.append(0)
    if age_list[index] >= 3 and age_list[index] <= 12:
      cost_list.append(14)
    if age_list[index] > 12 and age_list[index] < 65:
      cost_list.append(23)
    if age_list[index] >= 65:
        cost_list.append(18)
    index += 1
  
  return cost_list
  
def add_up(cost_list):
  index = 0
  total = 0
  
  for x in range(len(cost_list)):
    total += cost_list[index]
    index += 1
  
  return total
    
def main():
  age_list = take_input()
  cost_list = age_values(age_list)
  total = add_up(cost_list)
  print("%0s%.2f" % ("Total: $", total))
  
main()
def take_input():
  age_list = []
  age = "A"
  while True:
    age = input("What is the age? ")
    if age == "":
      break
    age_list.append(int(age))
  return age_list
  
def age_values(age_list):
  index = 0
  cost_list = []
  for x in range(len(age_list)):
    if age_list[index] <= 2:
      cost_list.append(0)
    if age_list[index] >= 3 and age_list[index] <= 12:
      cost_list.append(14)
    if age_list[index] > 12 and age_list[index] < 65:
      cost_list.append(23)
    if age_list[index] >= 65:
        cost_list.append(18)
    index += 1
  
  return cost_list
  
def add_up(cost_list):
  index = 0
  total = 0
  
  for x in range(len(cost_list)):
    total += cost_list[index]
    index += 1
  
  return total
    
def main():
  age_list = take_input()
  cost_list = age_values(age_list)
  total = add_up(cost_list)
  print("%0s%.2f" % ("Total: $", total))
  
main()
  
