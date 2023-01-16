
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

#Q9 Use tuple unpacking to save the values of the above tuple into variables.  
unpacked_tuples  = converte_list

print(unpacked_tuples)
