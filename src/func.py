# define doubeling function that passes args by value

num = 400


def mult(n):
    # n = 20
    return n * 2


print(num)
print(mult(num))
print(num)

# define doubeling function that passes args by reference

nums = [12, 3, 4, 34, 100, 10]


def list_doubler(l):
    for i in range(len(l)):
        l[i] *= 2
    # return l


print(nums)
print(list_doubler(nums))
print(nums)
