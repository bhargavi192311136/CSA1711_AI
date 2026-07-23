# List Methods
my_list = [1, 2, 3]

# Add (insert at position)
my_list.insert(1, 10)   # [1, 10, 2, 3]

# Append (add at end)
my_list.append(20)      # [1, 10, 2, 3, 20]

# Extend (add multiple elements)
my_list.extend([30, 40]) # [1, 10, 2, 3, 20, 30, 40]

# Delete (remove specific element)
my_list.remove(10)      # [1, 2, 3, 20, 30, 40]

# Delete using pop (by index)
my_list.pop(2)          # removes element at index 2

# Delete using del
del my_list[0]          # removes first element

print("Final List:", my_list)
