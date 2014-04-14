# This is the file you'll use to submit most of Lab 0.

# Certain problems may ask you to modify other files to accomplish a certain
# task. There are also various other files that make the problem set work, and
# generally you will _not_ be expected to modify or even understand this code.
# Don't get bogged down with unnecessary work.


# Section 1: Problem set logistics ___________________________________________

# This is a multiple choice question. You answer by replacing
# the symbol 'fill-me-in' with a number, corresponding to your answer.

# You get to check multiple choice answers using the tester before you
# submit them! So there's no reason to worry about getting them wrong.
# Often, multiple-choice questions will be intended to make sure you have the
# right ideas going into the problem set. Run the tester right after you
# answer them, so that you can make sure you have the right answers.

# What version of Python do we *recommend* (not "require") for this course?
#   1. Python v2.3
#   2. Python v2.5 or Python v2.6
#   3. Python v3.0
# Fill in your answer in the next line of code ("1", "2", or "3"):

ANSWER_1 = '2'


# Section 2: Programming warmup _____________________________________________

# Problem 2.1: Warm-Up Stretch

def cube(x):
	"""
	x: int or float
	returns cube of x
	"""
	return x**3

def factorial(x):
	"""
	x: non-negative integer
	returns factorial of x
	"""
	assert isinstance(x, int) and x >= 0, "factorial: input must be non-negative integer"
	if x == 1 or x == 0:
		return 1
	else:
		return x*factorial(x-1)


def count_pattern(pattern, lst):
	"""
	pattern: list of symbol
	lst: list to search in

	count_pattern( ['a', 'b'], ['a', 'b', 'c', 'e', 'b', 'a', 'b', 'f'] ) should return 2
	count_pattern( ['a', 'b', 'a'], ['g', 'a', 'b', 'a', 'b', 'a', 'b', 'a']) should return 3

	returns an int, counts number of times pattern appears in lst
	"""
	count = 0
	for i in range(len(lst) - len(pattern) + 1):
		listSlice = lst[i:len(pattern) + i]
		if sum([1 for i,j in zip(pattern, listSlice) if i==j]) == len(pattern):
			count += 1
	return count


# Problem 2.2: Expression depth

def depth(expr):
	"""
	expr: list
	return the depth of expr 
	"""
	if isinstance(expr, list):
		return 1 + max(depth(item) for item in expr)
	else:
		return 0

# Problem 2.3: Tree indexing

def tree_ref(tree, index):
	for a in index:
		tree = tree[a]
	return tree
    # raise NotImplementedError


# Section 3: Symbolic algebra

# Your solution to this problem doesn't go in this file.
# Instead, you need to modify 'algebra.py' to complete the distributer.

from algebra import Sum, Product, simplify_if_possible
from algebra_utils import distribution, encode_sumprod, decode_sumprod

# Section 4: Survey _________________________________________________________

# Please answer these questions inside the double quotes.

# When did you take 6.01?
WHEN_DID_YOU_TAKE_601 = "didnt take this class"

# How many hours did you spend per 6.01 lab?
HOURS_PER_601_LAB = "dont remember"

# How well did you learn 6.01?
HOW_WELL_I_LEARNED_601 = "didnt take 6.01"

# How many hours did this lab take?
HOURS = "few hours"


# print depth([1, 2, 3]) # 1
sample_tree = [[[1, 2], 3], 7, [4, [5, 6]], [8, 9, 10]]
print tree_ref(sample_tree, [3,1])
