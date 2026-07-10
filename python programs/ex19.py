c=int(input("How many elements: ")) 
list1=[] 
for i in range(c): 
          list1.append(int(input("Enter the element: "))) 
for i in list1: 
      if(i%2==0): 
           list1.remove(i) 
print(list1) 



def total_jumps(heights, X, Y):
    total = 0

    for h in heights:
        jumps = 1
        reach = X

        while reach < h:
            reach += (X - Y)
            jumps += 1

        total += jumps

    return total


# Example
print(total_jumps([11, 11], 10, 1))        # 4
print(total_jumps([11, 10, 10, 9], 10, 1)) # 5