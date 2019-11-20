import matplotlib
#matplotlib.use('Agg')
from numpy import *
import pandas as pand
from random import gauss
import scipy.stats as stats 

#Sub_Critico
C1=array(pand.read_csv('output_1D_n101_G042_1_', sep=" "))
C2=array(pand.read_csv('output_2D_n121_G170_1_', sep=" "))
C3=array(pand.read_csv('output_3D_n125_G190_1_', sep=" "))

#Super_Critico
C4=array(pand.read_csv('output_1D_n101_G100_1_10000'+'.log', sep=" "))
C5=array(pand.read_csv('output_2D_n121_G500_1_10000'+'.log', sep=" "))
C6=array(pand.read_csv('output_3D_n125_G600_1_10000'+'.log', sep=" "))




dbin_=0.05
bin_=arange(0, 10+dbin_, dbin_)
bin_[-1]=10000

met_est=C1[:,3]
##
m_met=mean(met_est)
v_met=var(met_est)
##
met_est=met_est/m_met
T_1=met_est

met_est2=C2[:,3]
m_met2=mean(met_est2)
v_met2=var(met_est2)
met_est2=met_est2/m_met2
T_2=met_est2

met_est3=C3[:,3]
m_met3=mean(met_est3)
v_met3=var(met_est3)
met_est3=met_est3/m_met3
T_3=met_est3

met_est4=C4[:,3]
m_met4=mean(met_est4)
v_met4=var(met_est4)
met_est4=met_est4/m_met4
T_4=met_est4

met_est5=C5[:,3]
m_met5=mean(met_est5)
v_met5=var(met_est5)
met_est5=met_est5/m_met5
T_5=met_est5

met_est6=C6[:,3]
m_met6=mean(met_est6)
v_met6=var(met_est6)
met_est6=met_est6/m_met6
T_6=met_est6

print(C1[0,2],'n',int(C1[0,1]),'m=', m_met, 'var=', v_met)
print(C2[0,2],'n',int(C2[0,1]),'m=', m_met2, 'var=', v_met2)
print(C3[0,2],'n',int(C3[0,1]),'m=', m_met3, 'var=', v_met3)

x=arange(0.01, 10, 0.1)
y=exp(-x)


import matplotlib.pyplot as plt
#plt.figure(figsize=(10,7))
plt.figure(figsize=(10,11))

#plt.subplot(3,2,1)
plt.subplot2grid((11, 9), (0, 0), colspan=4, rowspan=3)
n2, bins2, patches2 = plt.hist(T_1, bins = bin_, density=True, color=['darkblue'], label= r'$\gamma='+str("%.3f" % C1[0,2])+' \ \ n='+str(int(C1[0,1]))+'$')
plt.plot(x,y, color='red', label=r'$e^{-t} $')
plt.legend()
plt.xlim(0,7)
plt.ylim(0,1.1)
plt.text(4.9, 0.98, r'Lattice $\mathbb{Z}^1 $', fontsize=13)
plt.text(0.1, 1.02, 'a', fontsize=15,fontweight='bold')
#plt.title(r'lattice $\mathbb{Z}^1 $')  
#plt.xlabel('Normalized Time (t)')
plt.ylabel('Density');


#plt.subplot(3,2,3)
#plt.subplot2grid((7, 9), (4, 0), colspan=4, rowspan=3)
plt.subplot2grid((11, 9), (4, 0), colspan=4, rowspan=3)
n1, bins1, patches1 = plt.hist(T_2, bins = bin_, density=True, color=['darkgreen'], label= r'$\gamma='+str(C2[0,2])+' \ \ n='+str(int(C2[0,1]))+'$')
plt.plot(x,y, color='red', label=r'$e^{-t} $')
plt.legend()
plt.xlim(0,7)
plt.ylim(0,1.1)
plt.text(4.9, 0.98, r'Lattice $\mathbb{Z}^2 $', fontsize=13)
plt.text(0.1, 1.02, 'b', fontsize=15,fontweight='bold')
#plt.title(r'lattice $\mathbb{Z}^2 $')  
#plt.xlabel('Normalized Time (t)')
plt.ylabel('Density');

#plt.subplot(3,2,5)
plt.subplot2grid((11, 9), (8, 0), colspan=4, rowspan=3)
n3, bins3, patches3 = plt.hist(T_3, bins = bin_, density=True, color=['gray'], label= r'$\gamma='+str(C3[0,2])+' \ \ n='+str(int(C3[0,1]))+'$')
plt.plot(x,y, color='red', label=r'$e^{-t} $')
plt.xlim(0,7)
plt.ylim(0,1.1)
#plt.title(r'lattice $\mathbb{Z}^3 $')  
plt.xlabel('Normalized Time (t)')
plt.ylabel('Density');
plt.text(4.9, 0.98, r'Lattice $\mathbb{Z}^3 $', fontsize=13)
plt.text(0.1, 1.02, 'c', fontsize=15,fontweight='bold')
plt.legend(loc='best')



plt.subplot2grid((11, 9), (0, 5), colspan=4, rowspan=3)
n2, bins2, patches2 = plt.hist(T_4, bins = bin_, density=True, color=['darkblue'], label= r'$\gamma='+str("%.3f" % C4[0,2])+' \ \ n='+str(int(C1[0,1]))+'$')
#plt.plot(x,y, color='red', label=r'$e^{-t} $')
plt.legend()
plt.xlim(0,7)
plt.ylim(0,1.7)
plt.text(4.9, 1.25, r'Lattice $\mathbb{Z}^1 $', fontsize=13)
plt.text(0.1, 1.57, 'd', fontsize=15,fontweight='bold')
#plt.xlabel('Normalized Time (t)')
#plt.ylabel('Density');


#plt.subplot(3,2,3)
#plt.subplot2grid((7, 9), (4, 0), colspan=4, rowspan=3)
plt.subplot2grid((11, 9), (4, 5), colspan=4, rowspan=3)
n1, bins1, patches1 = plt.hist(T_5, bins = bin_, density=True, color=['darkgreen'], label= r'$\gamma='+str(C5[0,2])+' \ \ n='+str(int(C2[0,1]))+'$')
#plt.plot(x,y, color='red', label=r'$e^{-t} $')
plt.legend()
plt.xlim(0,7)
plt.ylim(0,1.7)
plt.text(4.9, 1.25, r'Lattice $\mathbb{Z}^2 $', fontsize=13)
plt.text(0.1, 1.57, 'e', fontsize=15,fontweight='bold')
#plt.title(r'lattice $\mathbb{Z}^2 $')  
#plt.xlabel('Normalized Time (t)')
#plt.ylabel('Density');

#plt.subplot(3,2,5)
plt.subplot2grid((11, 9), (8, 5), colspan=4, rowspan=3)
n3, bins3, patches3 = plt.hist(T_6, bins = bin_, density=True, color=['gray'], label= r'$\gamma='+str(C6[0,2])+' \ \ n='+str(int(C3[0,1]))+'$')
#plt.plot(x,y, color='red', label=r'$e^{-t} $')
plt.xlim(0,7)
plt.ylim(0,1.7) 
plt.xlabel('Normalized Time (t)')
plt.text(4.9, 1.25, r'Lattice $\mathbb{Z}^3 $', fontsize=13)
plt.text(0.1, 1.57, 'f', fontsize=15,fontweight='bold')
plt.legend(loc='best')




#plt.savefig('Histogram' +  '_n='+str(int(C1[0,1]))+ '_gamma='+str("%.3f" % C1[0,2])+ '.png',dpi=300)
plt.savefig('Histogram_Linear_Sub_Sup' +'.png',dpi=300)
#	close()
plt.show()

