# Tips and Tricks Links

# https://www.codementor.io/sumit12dec/python-tricks-for-beginners-du107t193
# https://sahandsaba.com/thirty-python-language-features-and-tricks-you-may-not-know.html

################ FOR LOOPS ################

#%% For loop with two lists
>>> for x, y in zip(list1,list2):
...    print x, y
...

#%% Numerate with a list
>>> a = ['Hello', 'world', '!']
>>> for i, x in enumerate(a):
...     print '{}: {}'.format(i, x)

#%% get key and value from dictionary
>>> m = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
>>> for k, v in m.iteritems():
...     print '{}: {}'.format(k, v)


################ LISTS ################

#%% fuse sub list to one list
import itertools
a = [[1, 2], [3, 4], [5, 6]]
>>> list(itertools.chain.from_iterable(a))
[1, 2, 3, 4, 5, 6]


#%% Sliding windows (n-grams) using zip and iterators
from itertools import islice
def n_grams(a, n):
	z = (islice(a, i, None) for i in range(n))
	return zip(*z)

a = [1, 2, 3, 4, 5, 6]
print(list(n_grams(a, 2)))
print(list(n_grams(a, 3)))
print(list(n_grams(a, 4)))

#%% flatten a list
a = [1, 2, [3, 4], [[5, 6], [7, 8]]]
flatten = lambda x: [y for l in x for y in flatten(l)] if type(x) is list else [x]
flatten(a)

#%% Histogram Collection counter table
import collections
A = collections.Counter([1, 2, 2])
B = collections.Counter([2, 2, 3])
print(A)
print(B)
print(A | B)
print(A & B)

A = collections.Counter([1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 6, 7])
A.most_common(1)

#%% Create a Json by hand
import json
tree = lambda: collections.defaultdict(tree)
root = tree()
root['menu']['id'] = 'file'
root['menu']['value'] = 'File'
root['menu']['menuitems']['new']['value'] = 'New'
root['menu']['menuitems']['new']['onclick'] = 'new();'
root['menu']['menuitems']['open']['value'] = 'Open'
root['menu']['menuitems']['open']['onclick'] = 'open();'
root['menu']['menuitems']['close']['value'] = 'Close'
root['menu']['menuitems']['close']['onclick'] = 'close();'
print json.dumps(root, sort_keys=True, indent=4, separators=(',', ': '))


#%% Get N max or N min
a = [random.randint(0, 100) for __ in xrange(100)]
heapq.nsmallest(5, a)
heapq.nlargest(5, a)


######################### KOMBINATORIK

#%% Combine all possibilities of those two lists
for p in itertools.product([1, 2, 3], [4, 5]):
	print(''.join(str(x) for x in p))

for p in itertools.product([0, 1], repeat=4):
	print(''.join(str(x) for x in p))

# take list a list of the length N for all combinations
for c in itertools.combinations([1, 2, 3, 4, 5], 3):
	 print(''.join(str(x) for x in c))

# Permutation; Give out all possible FORMATION of this list
for p in itertools.permutations([1, 2, 3, 4]):
	 print(''.join(str(x) for x in p))


import pandas as pd
import numpy as np
ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
ts.plot()
plt.show()