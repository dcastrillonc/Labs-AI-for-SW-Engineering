# Javascript/NodeJS Snippet
import os
import random

def menu():
  """Displays the menu options."""
  menu_string = "1. Show Menu\n"
  menu_string += "2. Add Numbers\n"
  menu_string += "3. Subtract Numbers\n"
  menu_string += "4. Quit\n"
  return menu_string

def clear_screen():
  """Clears the terminal screen."""
  os.system('cls' if os.name == 'nt' else 'clear')

def add_numbers():
  """Prompts the user for two numbers and adds them."""
  num1 = float(input("Enter the first number: "))
  num2 = float(input("Enter the second number: "))
  result = num1 + num2
  print(f"The sum is: {result}")

def subtract_numbers():
  """Prompts the user for two numbers and subtracts them."""
  num1 = float(input("Enter the first number: "))
  num2 = float(input("Enter the second number: "))
  result = num1 - num2
  print(f"The difference is: {result}")

# Main Program Starts
choice = 0

while choice < 4:
  clear_screen()
  print(menu())
  choice = int(input("Enter your choice: "))

  if choice == 1:
    clear_screen()
  elif choice == 2:
    add_numbers()
  elif choice == 3:
    subtract_numbers()
  else:
    break  # Exit the loop if choice is 4 (Quit)

print("Exiting the program...")