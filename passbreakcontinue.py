#break
nums = [1, 7, 45, 3, 6, 66, 88, 0]
count = 0
while count < 8:
  print(nums[count])
  count += 1
  if nums[count] == 66:
    break
print("Stop we encountered a 66")

#continue
for i in range(1, 45):

  if i == 22:
    continue
  else:
    print(i)

print("we encountered a 22")

#pass
for letter in 'Python':
   if letter == 'y':
      pass
      print('block pass')
   print('pointer :', letter)

