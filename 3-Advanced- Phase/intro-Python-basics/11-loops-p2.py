#Loops Control Statements
#break statement (using the break statement to exit a loop) 
#continue statement (using the continue statement to skip an iteration)

#for loop control statements
names = ["john", "taps", "jazzi", "PacMan", "T-Man"]
   
for name in names:
  if name == "jazzi":
    break  # Exit the loop when "jazzi" is found
  print(name)

print()

for name in names:
  if name == "jazzi":
    continue # Skip the iteration when "jazzi" is found 
  print(name)

#while loop control statements
count = 0 
while count < 5:
  print(count)
  count = count + 1
  if count == 3:
    break  # Exit the loop when count reaches 3 
  
print()

while count < 5:
  print(count)
  count = count + 1
  if count == 3:
   continue  # Skip the iteration when count reaches 3

