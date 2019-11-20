import matplotlib
matplotlib.use('Agg')
from numpy import *
import random
from pandas import *

for seed_ in range (1,1000): 
	random.seed(seed_)
	
	#Parametros
	N=50  #numero de neuronios 2N+1
	gama=0.028 #exponencia de tau_
	T=[]
	M=[]
	T=T+[0]
	M=M+[1]
	sparce=100*N #numero de interacao para salvar
	tsparce=0
	contador=0
	max_contador=10000
	#Periodo da semente random eh de 10^6.000
	###############Iniciando variaveis#################
	N=2*N+1
	V=ones(N)
	tau=zeros(2*N)
	run_con=(sum(V)/N)
	for i in range(N):
		tau[i]=-log(random.random())
		tau[i+N]=-(1.0/gama)*log(random.random())
	###################################################	
	#print ( N, gama)	

	i=sparce
	#for i in range(200):
	#while run_con > 1.0/N:
	while ((run_con > 0) & (contador<max_contador)):
		################ Evento #############################	
		t=min(tau)
		n=argmin(tau)

		if n<N:
			if V[n]>0:
				V[n]=0
				if n<N-1: 
					V[n+1]=V[n+1]+1
					u=1.0/(1.0+exp(-3*V[n+1]+6.0))
					tau[n+1]=t-(1.0/u)*log(random.random())
					
				if n>0: 
					V[n-1]=V[n-1]+1
					u=1.0/(1.0+exp(-3*V[n-1]+6.0))
					tau[n-1]=t-(1.0/u)*log(random.random())
		else: 
			V[n-N]=0

		#Sortear novos valores
		tau=tau-t
		#print(V)
		'''
		if n<N:
			tau[n]=-log(random.random())
		else:
			tau[n]=-(1.0/gama)*log(random.random())
		'''
		if n<N:
			tau[n]=1000
		else:
			tau[n]=-(1.0/gama)*log(random.random())
		
		run_con=(sum(V)/N)
		tsparce=tsparce+t
		i=i-1
		if i==0:
			T=T+[tsparce]
			M=M+[run_con]	
			i=i+sparce
			tsparce=0
			contador=contador+1
		#####################################################
	T=T+[tsparce]
	M=M+[run_con]	
	#i=i+sparce
	#tsparce=0


	################### Plot ################################
	for i in range(1,len(M)): T[i]=T[i]+T[i-1]
	'''
	import matplotlib.pyplot as plt
	plt.plot(T, M, 'k')
	#plt.scatter(T, M, '.r', markersize=0.5)
	plt.ylabel('media (S(1)/(2N+1))')
	plt.xlabel('tempo (s)')
	plt.ylim(0,1)
	plt.xlim(0,T[i])
	plt.savefig('plote_gama_' + str(gama) + '_n_'+str(N)+ '_seed_'+ str(seed_) + '_maxcontador_'+ str(max_contador)+'.png',dpi=300)
	'''
	print ( seed_, N, gama, T[i], contador)


	
	

	




