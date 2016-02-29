# copy the code from sum1.py into this file, THEN:
# change your program so it keeps reading numbers until it gets a -1, then prints the sum of all numbers read
sum =0
count=0
while count <10:
    count +=1
    num = (input(">>>"))
    num = float(num)
    if num == (0-1.0):
        count = 10
        sum += 1
    sum = sum + num
print(sum)