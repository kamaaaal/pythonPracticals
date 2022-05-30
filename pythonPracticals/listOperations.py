# list operation

# create a list using [] brackets
colleges = ['new college','srm','siet']

# appending a new value to list using .append() method
colleges.append('guru nanak')
print('colleges list after apending : ',colleges)

# insert a new value to a list with insert method
colleges.insert(2,'st.Joseph')
print('colleges list after inserting',colleges)

#remove an element using .remove() method
colleges.remove('srm')
print('colleges list after removing srm',colleges)

# remove an element using del keyword
del colleges[3]
print('colleges list after deleting 3rd element ',colleges)



