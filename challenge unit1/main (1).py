# Get input from the user
year = int(input("Enter a year: "))

# Check if it's a leap year or not
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print(f"{year} is a leap year")
    else:
      print(f"{year} is not a leap year")
  else:
    print(f"{year} is a leap year")
else:
  print(f"{year} is not a leap year")
