# Sets - It Can Not Have Duplicates
# Sets Are Also Unordered
 
s = {"Blueberry", "Raspberry"}

# Example Of Duplicates (Not Added)
s.add("Bluberry")
# Print S
print(s)

# Creating A List To Show No Duplicates
l = [1, 1, 2, 4, 6, 8, 6]

# Converting List To Set

no_duplicates_set  = set(l)
print(no_duplicates_set)

# Converting Set To List With No Duplicates
no_duplicates_list = list(l)
print(no_duplicates_list)

# Function union - Joins Two Sets
library_1 = {"Harry Potter", "Lord Of Rings", "Evil Spy School"}
library_2 = {"Harry Potter", "Romeo And Julliet"}
all_books_in_town = library_1.union(library_2)
print(all_books_in_town)

# Function To Clear A Set
all_books_in_town.clear()
print(all_books_in_town)



