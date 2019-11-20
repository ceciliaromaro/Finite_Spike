# Finite_Spike
Programs base to run the Finite-Spike model

See publication https://arxiv.org/abs/1911.02609


All programs presented here were developed in python and can be run as “python name.py” or "python Finite_Spike_1D_loop_n101_G034_1_10.py &> output_1D_n101_G034_1_10 &” .

“Finite_Spike_1D_loop_n101_G034_1_10.py” presents the code-base to run lattice Z = 1. This code is specific configuration to run the 1 dimension Z network (1D) with 101 neurons (n101), gamma equal to 0.34 (G034) 10 turns (1_10). 

Follow this pattern, 
Finite_Spike_2D_loop_n121_G125_1_2.py presents the base code to run lattice Z=2;
Finite_Spike_3D_loop_n125_G180_1_10.py presents the base code to run lattice Z=3;
Linear_Spike_1D_loop_n101_G042_1_10.py presents the linear activation function base code to run linear function lattice Z=1;
Sigmoidal_Spike_1D_loop_n101_G0028_1_1000.py presents the sigmoid activation function base code to run linear function lattice Z=1;

Calcula_Histograma_Linear_Sub_Sup.py takes the previous presented codes output (output_1D…, ) and rise the histograms as showed in Histogram_linear_SubSuber.png.
