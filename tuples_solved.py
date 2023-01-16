
#Q1 Create a tuple called numbers that contains the integers 1, 2, and 3.
#Q2 Create a tuple called letters that contains the strings "a", "b", and "c".
numbers= 1,2,3
letters = "a","b","c"

#Q3 Print out the first item in the numbers tuple.
#Q4 Print out the last item in the letters tuple.
print(numbers[0])
print(letters[-1])

#Q5 Use the + operator to concatenate the numbers and letters tuples. Store the result in a new tuple called result.
#Q6 Print out the length of the result tuple.
results = numbers + letters
print(len(results))
#Q7 Use the in keyword to check if the integer 4 is in the result tuple.
if "4" in results == int:
    print("TRUE")

#Q8  Use the tuple() function to convert a list of integers [4, 5, 6] into a tuple.
def convert(converte_list):
	return tuple(converte_list)
converte_list = [4,5,6]
print(convert(converte_list))

'''
or 
newTuple = tuple([4,5,6])

'''

#Q9 Use tuple unpacking to save the values of the above tuple into variables.  
list1= (4,5,6)
unpacked_tuple1, unpacked_tuple2, unpacked_tuple3  = list1
print(unpacked_tuple1, unpacked_tuple2, unpacked_tuple3)


#Q10 Use the index() method to find the index of the string "b" in the letters tuple. 
val = (letters)  
print(val)  
index = val.index('b') 
print("Index of b is: ",index)  


#Q11 Use the count() method to find the number of occurrences of the integer 2 in the result tuple.
count = results.count('2')
print(count) 

#Q12 Use the enumerate() function to iterate over the result tuple, along with its index, and print out each item and its index.
enumerated_list = enumerate(results)
for index,value in enumerated_list:
    print(index,value)

