from art import logo
import os

def add(n1,n2):
  return n1 + n2

def sub(n1,n2):
  return n1 - n2

def mul(n1,n2):
  return n1 * n2

def div(n1,n2):
  return n1 / n2

operations={
  "+": add,
  "-": sub,
  "*": mul,
  "/": div,
}
def calculator():
  print(logo)
  num1 = float(input("What is the first number?:\n"))
  for operators in operations:
      print(operators)
  continue_program = True
    
  while continue_program:
    operation_symbol= input("\nPick an operation:\n")
    num2 = float(input("\nWhat is the next number?:\n"))
    calculation_function=operations[operation_symbol]
    answer=calculation_function(num1, num2)
    print(f"\n{num1} {operation_symbol} {num2}: {answer}")
    if input(f"\nType 'y' to continue calculating with {answer}, Type 'n' to start new calculation:\n").lower() == "y":
      num1=answer
    else:
      continue_program = False
      os.system('cls')
      calculator()

calculator()
