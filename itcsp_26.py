'''
Exercise 26
Two objects of type 'Tuple' are given.
Nest these objects into a single object of type 'Tuple' (tuple of the tuples) - lets name it 't3'. 
The result write to the console. Expected result:
INPUT: tuples t1, t2
t1 = ('PKO', 'MWG', 'POE')
t2 = ('OKO', 'GWM', 'EOP')
OUTPUT: t3  (('PKO', 'MWG', 'POE'), ('OKO', 'GWM', 'EOP'))

'''
t1 = ('PKO', 'MWG', 'POE')
t2 = ('OKO', 'GWM', 'EOP')

t3 = ((t1, ) + (t2, ))  
print("The nested tuple : " + str(t3))
