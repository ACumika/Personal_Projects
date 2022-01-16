function gradient_descent
% Example from Kutz. 
% Find the minimum of x^2 + 3y^2 using gradient descent

clear all

ff = @(x,y) x.^2 + 3*y.^2;
subplot(2,1,1), ezsurfc(ff)
subplot(2,1,2), ezcontour(ff)

x(1)=3; y(1)=2; % initial guess
f(1)=x(1)^2+3*y(1)^2; % initial function value

err(1) = 1;
tol = 10^(-6);

for j=1:100
   
    tau=(x(j)^2 +9*y(j)^2)/(2*x(j)^2 + 54*y(j)^2);
    x(j+1)=(1-2*tau)*x(j);  % update values
    y(j+1)=(1-6*tau)*y(j);
    f(j+1)=x(j+1)^2+3*y(j+1)^2;
    err(j+1) = abs(f(j+1)-f(j));
    
    if err(j+1)<tol  % check convergence
        break
    end
    
end
%semilogy(err(2:end)), grid on
disp(['iter=',num2str(j+1),', x = ',num2str(x(end)),...
    ', y=',num2str(y(end)),', f=',num2str(f(end))])