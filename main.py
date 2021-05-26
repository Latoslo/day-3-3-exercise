# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

# > `on every year that is evenly divisible by 4
# >   **except** every year that is evenly divisible by 100
# >     **unless** the year is also evenly divisible by 400`
#Write your code below this line 👇
if year % 4 == 0:
  if year % 100 == 0:
      if year % 400 == 0:
        print('line12: This is a leap year')
      else:
        print('line14: This is not a leap year') 
  else:
    print('line16: This is a leap year')
else:
  print('line18: This is not a leap year')


