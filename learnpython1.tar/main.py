x = eval(input('Enter a number: '))
print(x, 2*x, 3*x, 4*x, 5*x, sep='---')


x1 = eval(input('Enter first number: '))
x2 = eval(input('Enter second number: '))
x3 = eval(input('Enter Third number: '))
sum1 = x1+x2+x3
averag = sum1/3
print('The total of the three number', sum1, sep='= ')
print('The average of the three number', averag, sep='= ')

price = eval(input('Enter the meal price: '))
tipPer = eval(input('Enter the tip percentage: '))

tip =price + ((tipPer/100)*price)

print('Meal Price', price, sep=': ')
print('Total bill', tip, sep=': ')

