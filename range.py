# create a function that performs the same duty as python's range function

# results for python's range function
test = list(range(5, 10))
print(test)

# creating a function that does the same thing
def my_range(m, n):
    range = []
    while m <= n - 1:
        range.append(m)
        m += 1
    print(range)
        
my_range(5, 10)