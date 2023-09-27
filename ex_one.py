#operators with precedence 
print(10-4*2) #2
print((10-4)*2) #12
print(5*2//3) #3
print(5*(2//3)) #0
print(2**3**2) #512 2**(3**2)=2**9 right-left
print((2**3)**2) #64
x=y=z=1
#x=y=z+=2 error equality has high prcdnce
m=2
n=3
if(m==m or m==n) and m==1:
	print("yes")

else:
	print("and has high prcdnce")
print(~m)#-3
print(~10)#-11
print(m&n) #2
print(m|n) #3
print(m^n) #1
print((m^n)|m) #3
print(m^(n|m)) #1
print(~m+n-1) #-1
print(m>>1) #1
print(m<<1) #4
print(m>>1<<m) #4
