x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
# #Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1][0]=15
print(x)
# #Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name']= 'Bryant'
print(students)
# #In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)
# #Change the value 20 in z to 30
z[0]['y'] = 30
print(z)


students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
#2
def iterateDictionary(students):
    for student in students:
        print(f"first_name: {student['first_name']} last_name: {student['last_name']}")

iterateDictionary(students)


# def iterateDictionary(students):
#     for student in students:
#         for key , value in student.item:
#             print(f"{key} - {value}")



#3 
# def iterateDictionary2(key_name, otherlist):
#     for i in otherlist:
#         print(i[key_name])

# iterateDictionary2('first_name',students)



#4 



dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printinfo(dojo):

    for key, values in dojo.items():
        length = len(values)
        key_upper = key.upper()
        print(f"{length}{key_upper}")
        for value in values:
            print(value)
printinfo(dojo)