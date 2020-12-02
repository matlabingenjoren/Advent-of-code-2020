clear all; close all; clc

A=importdata('dec_1.txt');

for i =1:200
    for y=1:200
            output=A(i)+A(y);        
            if output == 2020
            I=i;
            Y=y;          
            end 
    end
end
a2=A(Y)*A(I)


%%
clc
for i =1:200
    for y=1:200
        for u=1:200
            output=A(i)+A(y)+A(u);        
            if output == 2020
            I=i;
            Y=y;
            U=u;           
            end 
        end
    end
end
A(Y)*A(I)*A(U)
