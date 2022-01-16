%% Example of least square calculation
clear all   % remove all variables from the workspace
clc         % clear command window

x = [0 1 2 3 4]' %data
y = [1 1 2 2 3]'
A = [x ones(size(x))]  % put data in a matrix
B = A'*A            %normal matrix
Aty = A'*y          %right-hand side
u = B\Aty           %solve the system to find the fit coefficients
e = y - A*u         %error
e2norm = norm(e,2)

% plot the fit on a finer grid
xfit = linspace(x(1),x(end),100);
yfit = u(1)*xfit + u(2);
plot(x,y,'s',xfit,yfit,'b-','LineWidth',2)
grid on; axis equal

% cell array of text options
txtoptions = {'Interpreter','latex','FontSize',18}; 
xlabel ('x',txtoptions{:}); ylabel ('y',txtoptions{:})

% add legendsand title
fiteqn = ['best fit: y =',num2str(u(1)),'x + ',num2str(u(2))];
legends = {'data', fiteqn};
legend(legends,txtoptions{:},'Location','NorthWest');
title('Least-squres fit to the data',txtoptions{:})

ax = gca;  %get current axis
ax.FontSize = 18; % change the font size of the axes labels 

