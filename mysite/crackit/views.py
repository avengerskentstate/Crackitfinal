from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def index(request):
    return render(request, 'index.html')
def help(request):
    return render(request, 'help.html')
def end(request):
    return render(request, 'end.html')
def start(request):
	p = []
	i=random.randint(1,3)
	for x in range(0,5) :
		p.append(i)
		i=i+1
	q = []
	q.append(p[4]+4)
	q.append(p[4]-2)
	q.append(p[4]-1)
	q.append(p[4]+7)
	return render(request, 'start.html',{'content':[p[0],p[1],p[2],p[3]],'result':[p[4]],'n1':[q[0]],'n2':[q[1]],'n3':[q[2]],'n4':[q[3]]})
	
def start1(request):
	p = []
	for i in range(1,6) :
		p.append(3*i)
	q = []
	q.append(p[4]+4)
	q.append(p[4]-2)
	q.append(p[4]-1)
	q.append(p[4]+7)
	return render(request, 'start1.html',{'content':[p[0],p[1],p[2],p[3]],'result':[p[4]],'n1':[q[0]],'n2':[q[1]],'n3':[q[2]],'n4':[q[3]]})

def start2(request):
	p = []
	for i in range(0,5) :
		p.append(1+2*i)
	q = []
	q.append(p[4]+4)
	q.append(p[4]-2)
	q.append(p[4]-1)
	q.append(p[4]+7)
	return render(request, 'start2.html',{'content':[p[0],p[1],p[2],p[3]],'result':[p[4]],'n1':[q[0]],'n2':[q[1]],'n3':[q[2]],'n4':[q[3]]})

def start3(request):
	p = []
	for i in range(1,6) :
		p.append(i+1+2*i)

	q = []
	q.append(p[4]+4)
	q.append(p[4]-2)
	q.append(p[4]-1)
	q.append(p[1]+7)
	return render(request, 'start3.html',{'content':[p[0],p[1],p[2],p[3]],'result':[p[4]],'n1':[q[0]],'n2':[q[1]],'n3':[q[2]],'n4':[q[3]]})
	
def start4(request):
	p = []
	for i in range(1,6) :
	    p.append(i*i+i)
	q = []
	q.append(p[4]+4)
	q.append(p[4]-2)
	q.append(p[4]-1)
	q.append(p[4]+7)
	return render(request, 'start4.html',{'content':[p[0],p[1],p[2],p[3]],'result':[p[4]],'n1':[q[0]],'n2':[q[1]],'n3':[q[2]],'n4':[q[3]]})		

def start5(request):
	p = []
	for i in range(1,6) :
		if i%2==1:
			p.append(i+1)
		else :
			p.append(i-2)
	q = []
	q.append(p[4]+4)
	q.append(p[4]-2)
	q.append(p[4]-1)
	q.append(p[4]+7)
	return render(request, 'start5.html',{'content':[p[0],p[1],p[2],p[3]],'result':[p[4]],'n1':[q[0]],'n2':[q[1]],'n3':[q[2]],'n4':[q[3]]})

def start6(request):
	p = []
	for i in range(0,5) :
		p.append(3+5*i)
	q = []
	q.append(p[4]+4)
	q.append(p[4]-2)
	q.append(p[4]-1)
	q.append(p[4]+7)
	return render(request, 'start6.html',{'content':[p[0],p[1],p[2],p[3]],'result':[p[4]],'n1':[q[0]],'n2':[q[1]],'n3':[q[2]],'n4':[q[3]]})

def start7(request):
	p = []
	for i in range(1,10) :
	    if i%2==1:
               p.append(2*i+1) 
	q = []
	q.append(p[4]+4)
	q.append(p[4]-2)
	q.append(p[4]-1)
	q.append(p[4]+7)
	return render(request, 'start7.html',{'content':[p[0],p[1],p[2],p[3]],'result':[p[4]],'n1':[q[0]],'n2':[q[1]],'n3':[q[2]],'n4':[q[3]]})

def start8(request):
	p = []
	for i in range(2,7) :
	   p.append(i*i*i) 
	q = []
	q.append(p[4]+4)
	q.append(p[4]-2)
	q.append(p[4]-1)
	q.append(p[4]+7)
	return render(request, 'start8.html',{'content':[p[0],p[1],p[2],p[3]],'result':[p[4]],'n1':[q[0]],'n2':[q[1]],'n3':[q[2]],'n4':[q[3]]})

def start9(request):
	p = [1,1,2,3,5]
	q = []
	q.append(p[4]+4)
	q.append(p[4]-2)
	q.append(p[4]-1)
	q.append(p[4]+7)
	return render(request, 'start9.html',{'content':[p[0],p[1],p[2],p[3]],'result':[p[4]],'n1':[q[0]],'n2':[q[1]],'n3':[q[2]],'n4':[q[3]]})

def start10(request):

	p = []
	for i in range(1,6) :
		p.append(4+6*i)
		
	q = []
	q.append(p[4]+4)
	q.append(p[4]-2)
	q.append(p[4]-1)
	q.append(p[4]+7)
	return render(request, 'start10.html',{'content':[p[0],p[1],p[2],p[3]],'result':[p[4]],'n1':[q[0]],'n2':[q[1]],'n3':[q[2]],'n4':[q[3]]})
def start11(request):
	p = [2,5,10,17,26]
	q = []
	q.append(p[4]+4)
	q.append(p[4]-2)
	q.append(p[4]-1)
	q.append(p[4]+7)
	return render(request, 'start11.html',{'content':[p[0],p[1],p[2],p[3]],'result':[p[4]],'n1':[q[0]],'n2':[q[1]],'n3':[q[2]],'n4':[q[3]]})

def start12(request):
	p = [1,3,6,10,15]       
	q = []
	q.append(p[4]+4)
	q.append(p[4]-2)
	q.append(p[4]-1)
	q.append(p[2]+7)
	return render(request, 'start12.html',{'content':[p[0],p[1],p[2],p[3]],'result':[p[4]],'n1':[q[0]],'n2':[q[1]],'n3':[q[2]],'n4':[q[3]]})

def start13(request):
	p = []
	for i in range(1,6) :
		if i%2==1:
			p.append(i+2*i);
		else :
			p.append(i+3*i);
	q = []
	q.append(p[4]+4)
	q.append(p[4]-2)
	q.append(p[4]-1)
	q.append(p[4]+7)
	return render(request, 'start13.html',{'content':[p[0],p[1],p[2],p[3]],'result':[p[4]],'n1':[q[0]],'n2':[q[1]],'n3':[q[2]],'n4':[q[3]]})
	
def start14(request):
	p = []
	for i in range(1,7) :
		if i%2==1:
			p.append(i);
		else :
			p.append(i*2);
	q = []
	q.append(p[4]+4)
	q.append(p[4]-2)
	q.append(p[4]-1)
	q.append(p[4]+8)
	return render(request, 'start14.html',{'content':[p[0],p[1],p[2],p[3],p[4]],'result':[p[5]],'n1':[q[0]],'n2':[q[1]],'n3':[q[2]],'n4':[q[3]]})		

