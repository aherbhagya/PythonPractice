#!/usr/bin/python
#for printing square of 1 to 10 only even no
result=[x**2 for x in range(1,10) if x%2==0]
print result

# print the table
result1=[5*x for x in range(1,10+1)]
print result1
# print all odd no in between 1 to 50
result2=[x for x in range(0,50) if x%2!=0 ]
print result2
# convert lover to upper
result3=[x.upper() for x in ['q','w','e','r','t','f','g','k']]
print result3

result4=[x.lower() for x in ['A','F','H','T','MAHESH','KEDAR','sads']]
print result4

string='mahesh langote 24 male 787474 nanded 10 aug'
result5=[x for x in string if x.isdigit()]
print result5

mix_list=['mahesh','langote','male','python','angularjs','js',24]
result6=[(key,value) for key,value in enumerate(mix_list)]

print result6 #enumerate
lst=range(1,11)
print lst