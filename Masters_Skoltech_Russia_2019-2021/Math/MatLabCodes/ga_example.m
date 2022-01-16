function ga_example
clear all

% some data with noise
n = 30;
xx = linspace(0,2*pi,n);
yy = 3*cos(2*xx) + 1 + 0.2*rand(1,n); 

[x,fval, flag] = ga(@(x)fit_line(x),3,[],[],[],[],[],[])
%x = ga('fit',n,A,b,Abar,bbar,xl,xu,nonlin,options)

yfit = x(1)*cos(x(2)*xx) + x(3);
plot(xx,yy,'ro',xx,yfit,'b-x')
grid on

function E = fit_line(x)
    
    E = sum((x(1)*cos(x(2)*xx) + x(3) - yy).^2);

end

end
