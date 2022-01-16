function fminsearch_example
% uses Nelder-Meade method to find the minimum
% c = [14.6, 0.21, 63.0]

x = 1:24;   % raw data
y = [75 77 76 73 69 68 63 59 57 55 54 52 ...
   50 50 49 49 49 50 54 56 59 63 67 72];

plot(x,y,'ko')
grid on

% pause 

[c fval] = fminsearch(@datafit,[12 pi/12 63]) % optimization

xx=1:0.01:24;
yfit = c(1)*cos(c(2)*xx) + c(3);


txtoptions = {'Interpreter','latex','FontSize',18}; 
plot(x,y,'ko',xx,yfit,'k-'); grid on
xlabel ('x',txtoptions{:})
ylabel ('y',txtoptions{:})
legend({'data','$$y = c_1 \cos(c_2 x) + c_3$$'},txtoptions{:},'Location','NorthEast');
title({'Data and their fit using fminsearch, c = ',num2str(c)},txtoptions{:})

function e2 = datafit(c)

    e2 = sqrt(sum((c(1)*cos(c(2)*x)+c(3) - y).^2)/24);
 
end
end


