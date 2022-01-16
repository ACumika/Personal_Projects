%% Example 2 from Kutz, 15.5
clear all   % remove all variables from the workspace
clc         % clear command window
clf         % clear figure

x = linspace(-10,10,100);
t = linspace(0,10,30);

[X T] = meshgrid(x,t);

f0 = @(X,T) sech(X).*(1 - 0.5*cos(2*T)) + (sech(X).*tanh(X)).*(1 - 0.5*sin(2*T));

iimax = length(t);

figure(1)

for ii = 1:iimax 
plot(x,f0(X,T(ii)),'k','Linewidth',2)
axis([-10 10 -0.5 2 ])
grid on
pause(0.1)

end

%pause

f = sech(X).*(1 - 0.5*cos(2*T)) + (sech(X).*tanh(X)).*(1 - 0.5*sin(2*T));

figure(2)
subplot(2,2,1), waterfall(X,T,f), colormap([0 0 0]) 

[u, s, v] = svd(f');

for j=1:3
    ff = u(:,1:j)*s(1:j,1:j)*v(:,1:j)'; %modal projections
    subplot(2,2,j+1)
    waterfall(X,T,ff'), colormap([0 0 0])
    set(gca,'Zlim',[-1 2])
end

subplot(2,2,1), text(-19, 5, -1, '(a)','FontSize',14)
subplot(2,2,2), text(-19, 5, -1, '(b)','FontSize',14)
subplot(2,2,3), text(-19, 5, -1, '(c)','FontSize',14)
subplot(2,2,4), text(-19, 5, -1, '(d)','FontSize',14)

figure(3)

sig = diag(s);
subplot(3,2,1), plot(sig,'ko','Linewidth',2)
axis([0 25 0 50])
set(gca,'Fontsize',13,'Xtick',[0:5:25])
text(20,40,'(a)','Fontsize',13)
grid on

subplot(3,2,2), semilogy(sig,'ko','Linewidth',2)
axis([0 25 10^-(18) 10^5])
set(gca,'Fontsize',13,'Xtick',0:5:25,'Ytick', 10.^(-15:5:5));
text(20,10^0,'(b)','Fontsize',13)
grid on

energy1 = sig(1)/sum(sig)
energy2 = sum(sig(1:2))/sum(sig)

subplot(3,1,2) %spatial modes
plot(x,u(:,1),'k',x,u(:,2),'k--','Linewidth',2)
set(gca,'Fontsize',13)
legend('mode 1','mode 2','Location','NorthWest')
text(8, 0.35, '(c)', 'Fontsize',13)
grid on

subplot(3,1,3) %time evolution
plot(t,v(:,1),'k',t,v(:,2),'k--','Linewidth',2)
set(gca,'Fontsize',13)
legend('mode 1','mode 2','Location','NorthWest')
text(9, 0.35, '(d)', 'Fontsize',13)
grid on

pause

figure(4) %dynamics of modes 1 and 2 separately

for ii = 1:iimax 
ff1 = u(:,1)*s(1,1)*v(ii,1)'; % the mode 1 at time ii 
ff2 = u(:,2)*s(2,2)*v(ii,2)'; % the mode 2 at time ii 

subplot(2,1,1), plot(x,ff1,'k',x,ff2,'r','Linewidth',2)
axis([-10 10 -0.5 2 ])
grid on
legend('mode 1','mode 2')

subplot(2,1,2), plot(x,f0(X,T(ii)),'k-',x,ff1+ff2,'b:o','Linewidth',2)
axis([-10 10 -0.5 2 ])
legend('full function','mode 1+2')
grid on

pause(0.1)


end





