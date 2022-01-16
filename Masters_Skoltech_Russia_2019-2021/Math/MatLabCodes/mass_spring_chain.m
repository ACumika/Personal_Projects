%% Longitudinal oscillations in a chain of springs and masses. 
% Mathematical Methods in Engineering and Applied Science. Skoltech. Fall 2019. A. Kasimov
clear all; clf

xmax = 1; tend = 10; dt = 0.05;

set(gca,'nextplot','replacechildren'); grid on;
axis([0 xmax -1 1]); 

n = 3; %number of oscillating masses
h = xmax/(n+1); x = h*(1:n)';
Kn = 1/h^2*toeplitz([2 -1 zeros(1,n-2)])
[S, D]= eig(Kn);  
omega = sqrt(diag(D));

for j = 1:n    
    udot0 = 0*ones(size(x)); %initial conditions
    u0 = 0.1*S(:,j);
    
    a = inv(S)*u0; 
    b = inv(S)*udot0;  
    b = b./omega;
    
    for t=0:dt:tend
        v = a.*cos(omega*t) + b.*sin(omega*t);
        u = S*v;                %solution at t
        z = x + u + i*eps;      % complexify for plotting
        plot([0; z; xmax],'-o','LineWidth',4,'MarkerEdgeColor','k',...
            'MarkerFaceColor','k',  'MarkerSize',15)
        title(['Chain of ',num2str(n),' oscillators. Mode ',num2str(j)]);
        %drawnow;
        getframe;
    end
end