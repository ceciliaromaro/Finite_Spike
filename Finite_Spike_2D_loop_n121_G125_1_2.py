import matplotlib
matplotlib.use('Agg')
from numpy import *
import random
from pandas import *

for seed_ in range (1,2): 
	random.seed(seed_)

	#Parametros
	A=5  #numero de neuronios 2N+1
	gama=1.25 #exponencia de tau_
	T=[]
	M=[]
	T=T+[0]
	M=M+[1]
	sparce=1000*A*A # 100*N numero de interacao para salvar
	tsparce=0
	contador=0
	max_contador=1000 #100000
	#Periodo da semente random eh de 10^6.000
	###############Iniciando variaveis#################
	A=2*A+1
	N=A*A
	V=ones(N)
	tau=zeros(2*N)
	run_con=(sum(V)/N)
	for i in range(N):
		tau[i]=-log(random.random())
		tau[i+N]=-(1.0/gama)*log(random.random())
	###################################################	
	#print (A, N, gama)	

	i=sparce
	#for i in range(200):
	#while run_con > 1.0/N:
	while ((run_con > 0) & (contador<max_contador)):
	#if 1==1:
		################ Evento #############################	
		t=min(tau)
		n=argmin(tau)
		j=int(n/A)
		k=(n%A)
	
		if n<N:
			if V[n]==1:
				V[n]=0
				#if n<N-1: V[n+1]=1
				#if n>0: V[n-1]=1
				#Linha j fixa, olha colana k
				if k<A-1: V[n+1]=1
				if k>0: V[n-1]=1
				#Na coluna Fixa k, olha limite de linha
				if j<A-1: V[n+A]=1
				if j>0: V[n-A]=1
		else: 
			V[n-N]=0
	
		#Sortear novos valores
		tau=tau-t
		if n<N:
			tau[n]=-log(random.random())
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


	#plt.show()
	#'k'


	#figure(1)
	#figure(figsize=(20,5))
	#plot(i,M[i] , '.r', markersize=0.5)
	#xlabel('Time (ms)')
	#ylabel('Mean')
	#ylim(0,sum(N_))
	#xlim(-10,100)
	#xlim(0,tsimu/ms)
	#plt.gca().invert_yaxis()
	#show()
	#savefig('raster_w_p' +  '_wvtodo' + '.png',dpi=300)
		#savefig('raster_w_p' + str(w_p[0]) + '_wv' + str(wv) + '.png',dpi=300)
	#close()

	
	

	




