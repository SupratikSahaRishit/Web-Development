# take marks as input from user 
print("Enter marks of 4 subjects obtained in exam :")
math = int(input("maths :"))
english = int(input("english :"))
science = int(input("science :"))
business = int(input("business :"))
# Let's calculate the percentage of marks 
sum = math+english+science+business
print("sum of math , english , science and business")
perc = (sum/400)^100
print(end="Percentage mark =")
print("perc")