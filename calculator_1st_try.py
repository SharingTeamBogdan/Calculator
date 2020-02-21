import sys
def types():
	type_v=input()
	if(type_v=="float"):
		return 0
	elif(type_v=="int"):
		return 1
n=input("What type is your number? ")
if(n=='float'):
	x=float(input())
elif(n=='int'):
	x=int(input)
op=input()
if(op=="+"):
	if(types()==0):
		b=float(input())
		print(n+b)
	else:
		b=int(input())
		print(n+b)
	proceed=input("Do you wish to proceed? ")
	if(proceed=="no"):
		quit()
if(op=="-"):
	if(types()==0):
		b=float(input())
		print(n-b)
	else:
		b=int(input())
		print(n-b)
	proceed=input("Do you wish to proceed? ")
	if(proceed=="no"):
		quit()
if(op=="*"):
	if(types()==0):
		b=float(input())
		print(n*b)
	else:
		b=int(input())
		print(n*b)
	proceed=input("Do you wish to proceed? ")
	if(proceed=="no"):
		quit()
if(op=="/"):
	if(types()==0):
		b=float(input())
		print(n/b)
	else:
		b=int(input())
		print(n/b)
	proceed=input("Do you wish to proceed? ")
	if(proceed=="no"):
		quit()
if(op=="%" and type(n)=='<class> int'):
	b=int(input())
	print(n%b)
	proceed=input("Do you wish to proceed? ")
	if(proceed=="no"):
		quit()
if(op=="**"):
	b=int(input())
	print(n**b)
	proceed=input("Do you wish to proceed? ")
	if(proceed=="no"):
		quit()