def demonstrate_mutability():
    
    fruits = ["apple", "banana", "cherry"]
    
    print("Original List:", fruits)
    
 
    fruits[1] = "orange"
    print("List after modifying index 1:", fruits)
    

    fruits.append("grape")
    print("List after appending 'grape':", fruits)
    
  
    fruits.remove("apple")
    print("List after removing 'apple':", fruits)

    
    fruits.pop()
    print("List after popping the last item:", fruits)

demonstrate_mutability()
