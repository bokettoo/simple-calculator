firstnumber = int(input('please enter the first number'))
secondnumber = int(input('please enter the second number'))
op = str(input('enter the type of operation'))
if op == '+':
  print(firstnumber + secondnumber)
elif op == '-': 
  print(firstnumber-secondnumber)
elif op == '*': 
  print(firstnumber*secondnumber)
elif op == '/': 
  if secondnumber == 0 :
   print('error')
  else:
   print(firstnumber/secondnumber)
elif op == '%': 
  print(firstnumber%secondnumber)
else:
  print('error, try again')
