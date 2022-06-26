
from collections import namedtuple

Dog = ('Dog', ['age', 'breed', 'name'])


sam = Dog(age=2, breed='Lab', name='sammy')
frank = Dog(age=5, breed='Shepard', name='frankie')

print(sam[0])
