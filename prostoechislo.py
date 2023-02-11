for i in range(1,101):
	n = 2
	x = 0
	for e in range(1,i+1):
		if i % e ==0:
			x+=1
	if x == n:
  		  print(i)