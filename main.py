import random
import Calculator

rand_list = []


for i in range(20):
    number1 = random.randint(0, 100)
    rand_list.append(number1)
num1 = random.choice(rand_list)
num2 = random.choice(rand_list)
num_of_user = int(input("how many numbers do u want to add: "))
sum_list = []
for i in range(num_of_user):
    num = random.choice(rand_list)
    sum_list.append(num)
print(sum_list)
sub = Calculator.Subtraction()
add = Calculator.Addition()
div = Calculator.Division()
mul = Calculator.Multiplication()
sub = sub.subtract(num1, num2)
div = div.divide(num1, num2)
mul = mul.multiply(num1, num2)

add = add.add(sum(sum_list))
print(add)
print(sub)
print(div)
print(mul)
