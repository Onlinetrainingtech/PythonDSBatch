entry=0
sum=0
print("Enter the sum:")
while True:
    entry=eval(input())
    if entry<0:
        break
        #continue
    sum+=entry
print("Sum=:",sum)
