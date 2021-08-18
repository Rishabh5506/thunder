n=int(input('Enter the number of terms '))
a,b=0,1
print(a)
print(b)
i=1
while i<n-1:
c=a+b
print(c)
a,b=b,c
i=i+1
