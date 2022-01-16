%% Example 1 from Kutz, 15.5
clear all   % remove all variables from the workspace
clc         % clear command window
clf         % clear figure

x = linspace(0,1,25);
t = linspace(0,2,50);

[T, X] = meshgrid(t,x);

f = exp(-abs((X-0.5).*(T-1))) + sin(X.*T);

figure(1)
subplot(2,2,1), surfl(X,T,f), shading interp %, colormap gray 

[u, s, v] = svd(f);

for j=1:3
    ff = u(:,1:j)*s(1:j,1:j)*v(:,1:j)'; %modal projections
    subplot(2,2,j+1), surfl(X,T,ff), shading interp %, colormap gray
    set(gca,'Zlim',[0.5 2])
end

subplot(2,2,1), text(-0.5, 1, 0.5, '(a)','FontSize',14)
subplot(2,2,2), text(-0.5, 1, 0.5, '(b)','FontSize',14)
subplot(2,2,3), text(-0.5, 1, 0.5, '(c)','FontSize',14)
subplot(2,2,4), text(-0.5, 1, 0.5, '(d)','FontSize',14)

figure(2)

sig = diag(s);
energy1 = sig(1)/sum(sig)
energy3 = sum(sig(1:3))/sum(sig)

subplot(2,2,1), plot(sig,'ko','Linewidth',2)
axis([0 25 0 50])
set(gca,'Fontsize',13,'Xtick',[0 5 10 15 20 25])
text(20,40,'(a)','Fontsize',13)
grid on

subplot(2,2,2), semilogy(sig,'ko','Linewidth',2)
axis([0 25 10^-(18) 10^5])
set(gca,'Fontsize',13,'Xtick',[0:5:25],'Ytick', [10.^(-15:5:5)]);
text(20,10^0,'(b)','Fontsize',13)
grid on

subplot(2,1,2), plot(x,u(:,1),'k',x,u(:,2),'k--',x,u(:,3),'k:','Linewidth',2)
set(gca,'Fontsize',13)
legend('mode 1','mode 2', 'mode 3','Location','NorthWest')
text(0.8, 0.35, '(c)', 'Fontsize',13)
grid on

