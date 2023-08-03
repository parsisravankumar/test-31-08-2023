"""10. Write a program to remove all the tuples from a given list of tuples
 where the second element of the tuple is even number."""
l = [(1, 2, 3, 4, 5),
     (10, 11, 12, 13),
     (23, 14, 15, 17, 18),
     (25, 17, 34, 18, 7)]

l = [t for t in l if t[1] % 2 != 0]

print(l)