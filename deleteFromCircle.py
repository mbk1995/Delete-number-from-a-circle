import sys

def list_seq(n,m,k):
	a = list(range(n))
	l = len(a)

	# following steps are to obtain list in anticlockwise direction for ex:[0,9,8,7,6,5,4,3,2,1] 

	first_element=a[:1]
	temp = a[1:l+1]
	temp.reverse()
	lis = first_element + temp  # the list is formed in anti clockwise direction
	i = 0
	while len(lis) >k:   # the loop runs till last k elements are left
		s = len(lis) - m
		del lis[m-1]
		lis[:s], lis[s:] = lis[-s:], lis[:-s]  #starting the list from where it deleted the element eg [6,5,4,3,2,1,0,9,8]
	final_list = sorted(lis) 
	print "the last four numbers remaining are", final_list

def main():
	# input the values in the command window
	# run the code in "python deleteFromCircle.py 10 4 4 " format
	n= int(sys.argv[1])
	m = int(sys.argv[2])
	k= int(sys.argv[3])
	list_seq(n,m,k)

if __name__ == "__main__": main()
