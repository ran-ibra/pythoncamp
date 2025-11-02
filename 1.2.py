"""
Problem Description:
Write a program that takes a list of numbers and provides the following operations:
. Find the sum and average
. Find the maximum and minimum
. Remove duplicates
. Sort in ascending and descending order
. Filter even and odd numbers
Expected Output:
Enter numbers separated by spaces: 5 3 8 3 9 1 8 2
Original list: [5, 3, 8, 3, 9, 1, 8, 2]
Sum: 39 
Average: 4.875
Max: 9, Min: 1
Without duplicates: [5, 3, 8, 9, 1, 2]
Sorted (asc): [1, 2, 3, 5, 8, 9]
Even numbers: [8, 2]
Odd numbers: [5, 3, 9, 1]
Hints:
Use built-in functions: sum(), max(), min()
Use set() to remove duplicates
Use list comprehension for ltering
"""
inp = input("Enter nums in seperated spaces: ").split()
lis = [int(x )for x in inp]
print (f"Original list {lis}")
#input 

summ= sum(lis)
print(f"sum: {summ}")
avg = summ/ len(lis)
print(f"Average: {avg}")
maxx= max(lis)
minn= min(lis)
print(f"max {maxx}, min {minn}")

withoutdup= set(lis)
print(f"list without duplicates: {withoutdup}")

print(f"asc. order {sorted(lis)}")
print(f"desc. order {sorted(lis, reverse=True)}")
odd = [x for x in lis if x%2==1]
print (f"Odd numbers {odd}")
even = [x for x in lis if x%2==0]
print (f"Odd numbers {even}")

#print(f"Odd num { lambda x:x%2}")


