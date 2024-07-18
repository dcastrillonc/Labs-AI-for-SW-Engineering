def menu():
  """Displays the menu options."""
  menu_string = "1. Show Menu\n"
  menu_string += "2. Add Numbers\n"
  menu_string += "3. Subtract Numbers\n"
  menu_string += "4. Quit\n"
  return menu_string

# Main Program Starts
choice = 0

while choice < 4:
  print(menu())
  choice = int(input("Enter your choice: "))

  if choice == 1:
    # Clear the screen (implementation depends on your environment)
    print("\033c" if choice == 1 else "")  # Use ANSI escape code for clearing screen
  elif choice == 2:
    print("\n\nAdd Some Numbers\n\n")
    # Implement addition logic here
  elif choice == 3:
    print("\n\nSubtract some Numbers\n\n")
    # Implement subtraction logic here
  else:
    break  # Exit the loop if choice is 4 (Quit)
