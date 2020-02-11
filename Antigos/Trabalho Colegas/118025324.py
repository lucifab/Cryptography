def mdc(a,b):
	r=a%b
	mdc=r
	while(r>0):
		mdc=r
		a=b
		b=r
		r=a%b
	return mdc


def grupo(x):
	grupo=[1]
	for i in range(2,x):
		if(mdc(x,i)==1):
			grupo.append(i)
	return grupo


def pop1(x,sg):
	g=grupo(x)
	for i in range(len(sg)):
		flag=0
		for j in range(len(g)):
			if sg[i]==g[j]:
				flag=1
		if flag==0:
			return 0
	return 1


def pop2(x,sg):
	for i in range(len(sg)):
		for j in range(i,len(sg)):
			op=(sg[i]*sg[j])%x
			flag=0
			for k in range(len(sg)):
				if sg[k]==op :
					flag=1
			if flag==0:
				return 0

	return 1

def pop3(x,sg):
	for i in range(len(sg)):
		if(sg[i]%x==1):
			return 1
	return 0

def pop4(x,sg):
	for i in range(len(sg)):
		if(mdc(sg[i],x)!=1):
			return 0
	return 1


def esubgrupo(x,sg):
	if pop1(x,sg)==0 :
		return 0
	if pop2(x,sg)==0 :
		return 0
	if pop3(x,sg)==0 :
		return 0
	if pop4(x,sg)==0 :
		return 0
	return 1

n=input()
while(n>0):
	n-=1
	x,sg=input()
	
	igual="NAO"
	if(esubgrupo(x,sg)==1):
		igual="SIM"
	print igual
	print "---"