# When should you use a set?
# When you need to remove duplicates from a collection instantly.
# When you need fast lookups (checking if item in my_set runs in O(1) constant time, which is much faster than a list).
# When you need to compare two groups of data to find similarities or differences.

fr = {'banana', 'mango', 'orange'}
nums = [2,2,1,1,2,3,4,5,6,6,6,6,7,8]
u_nums = set(nums)
# print(u_nums)

empty_list = []
empty_dict = {}
empty_tuple = () #  you cannot append or add items to an empty tuple after it is created
empty_set = set()

# Characteristics of Sets:
# 1. NO duplicated
# 2. Unordered
# 3. Items must be Immutable (Hashable)

my_set = {1,2,3}
my_set.add(4)
my_set.update([6, 7])
my_set.remove(3)
my_set.discard(77)
# print(my_set)

# Venn Diagram Operations

group_a = {'a', 'b', 'c'}
group_b = {'c','d', 'e'}
# union
print(group_a | group_b)
# intersection
print(group_a & group_b)
#  difference
print(group_a - group_b)
# synthetic difference
print(group_a ^ group_b)

