#tuples

# numbers=(1,3,2,4,5)  #Tuple define by (),

# print(numbers[1])   #index positioning,duplicates allowed,immutable,methods=index(),count()



#tuple modification

numbers=[1,2[3,(100,200,300),4],5,6]  #[1,2[3,(100,200,300,500),4],5,6]

num=numbers[2][1]   #(100,200,300)

new_num=list(num)   #[100,200,300]

new_num.append(500)  #[100,200,300,500]

print(tuple(new_num))   #(100,200,300,500)

numbers[2][1] = tuple(new_num)   #[1,2[3,(100,200,300,500),4],5,6]

print(numbers)