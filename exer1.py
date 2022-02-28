#!/usr/bin/python3

#Exercise1. Modifiy print_matrix1 function to generate the same matrix found in:
#https://upload.wikimedia.org/wikipedia/commons/2/28/Smith-Waterman-Algorithm-Example-Step2.png
#or like sw.PNG

def print_matrix1(a,x,y):
    mrows = len(x)
    ncols = len(y)
    print(" ", end='  ')
    
    for i in range(ncols+1):
        if i == 0 or i > ncols:
            print(" ", end='  ')
        else:
            print("%s" % y[i-1], end='  ')
    print()
    
    for i in range(mrows+1):
        if i > 0:
            print("%s" % x[i-1], end=' ')
        else:
            print(" ", end=' ')
        for j in range(ncols+1):
            print("%2d" % a[i][j], end=' ')
        print()
        
def find_sequence(a,x,y):
    mrows = len(x)
    ncols = len(y)
    max_value = 0
    index = {}
    #find max value
    for i in range(mrows+1):
        for j in range(ncols+1):
            if a[i][j] > 0 and a[i][j] > max_value:
                max_value =  a[i][j]
                index["i"] = i
                index["j"] = j
    max_values=[]
    max_values.append(max_value)
    xI = index["i"]
    yI = index["j"]
    top = []
    bot = []
    nX = 1
    nY = 1
    #go to diagonals until letters are different
    while max_value!=0:
        if x[xI-nX] != y[yI-nY]:   
            top.append(x[xI-nX])
            bot.append("-")
            max_value =  a[xI-nX][yI-nY+1]
            max_values.append(max_value)
            nX = nX+1
        else:
            top.append(x[xI-nX])
            bot.append(y[yI-nY])
            max_value =  a[xI-nX][yI-nY]
            max_values.append(max_value)
            nX=nX+1
            nY=nY+1
       
    top.reverse()
    bot.reverse()
    print(max_values)
    print(*bot)
    print(*top)
    
def gen_matrix(x, y, match_score, gap_cost):
	mrows = len(x)
	ncols = len(y)
	#initialize matrix to zeroes
	a = [0] * (mrows + 1)
	for i in range(mrows + 1):
		a[i] = [0] * (ncols + 1)
	
	#print_matrix1(a,x,y)
	
	for i in range(1,mrows+1):
		for j in range(1,ncols+1):
			match = a[i-1][j-1] - match_score
			if(x[i-1] == y[j-1]):
				match = a[i-1][j-1] + match_score
			delete = a[i - 1][j] - gap_cost
			insert = a[i][j - 1] - gap_cost
			a[i][j]=max(match,delete,insert,0)

	#print_matrix(a,x,y)	
	return(a)
#'''	
x = "GGTTGACTA"	
y = "TGTTACGG"
match_score=3 
gap_cost=2

'''

x = "CAGACCTA"	
y = "CCGTACTA"
match_score=2 
gap_cost=1
'''

a=gen_matrix(x,y,match_score,gap_cost)


print_matrix1(a,x,y)
find_sequence(a,x,y)