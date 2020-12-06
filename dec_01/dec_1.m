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
a1=A(Y)+A(I);
a2=A(Y)*A(I);
format_a="Q1\n%d + %d = %d\n%d * %d = %d";
sprintf(format_a,A(Y),A(I),a1,A(Y),A(I),a2)

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
b1=A(Y)+A(I)+A(U);
b2=A(Y)*A(I)*A(U);
format_a="Q2\n%d + %d + %d = %d\n%d * %d * %d = %d";
sprintf(format_a,A(Y),A(I),A(U),b1,A(Y),A(I),A(U),b2)