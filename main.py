# Take marks as input from the user
print("Enter marks obtained in four subjects:")
math = int(input("maths :"))
english = int(input("english :"))
science = int(input("science :"))
french = int(input("french :"))

# Lets calculate the percentage of the marks
sum=math+english+science+french
print(" sum of math, english, science and french")

perc = (sum/400)*100

print( end="Percentage Mark = ")
print(perc)