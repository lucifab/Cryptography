def mdc(a,b):
	r=a%b
	mdc=r
	while(r>0):
		mdc=r
		a=b
		b=r
		r=a%b
	return mdc
