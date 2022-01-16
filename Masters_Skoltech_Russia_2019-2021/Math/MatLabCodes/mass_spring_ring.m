%% Oscillations in a chain of springs and masses on a ring. 
% Mathematical Methods in Engineering and Applied Science. Skoltech. Fall 2019. A. Kasimov
% n masses and springs on a circular ring

clear all; clc; clf

n = 4; 
Cn  = [2 -1 0 -1;-1 2 -1 0;0 -1 2 -1;-1 0 -1 2];
[S D]= eig(Cn);  lambda = diag(D);

for j = 1:n
    
    u0 =  0.5*( S(:,j) );   %initial displacement
    udot0 = (j==1).*pi/10*ones(size(u0));   %initial velocity, only nonzero if j=1, for which there should be rotation
    a = inv(S)*u0; 
    B = inv(S)*udot0;
    
    b(1) = B(1); 
    b(2:n) = B(2:n)./sqrt(lambda(2:n)); 
    b = b(:);

    %initial, rest position of the masses
    phi0 = 2*pi/n*(0:n-1)';     X = -sin(phi0);  Y = cos(phi0);

    %plus the initial displacements (angles)
    X = -sin(phi0 + u0); Y = cos(phi0 + u0);

    %set(gca, 'color', 'cyan');  set(gcf, 'color', 'yellow');  % uncomment this to add some color
    grid on;   axis([-1 1 -1 1]*1.2);  axis equal
    set(gca,'nextplot','replacechildren')

    % plot tsteps solutions at t from 0 to tend
    tend = 20; tsteps = 100; dt = tend/tsteps; t = dt*(1:tsteps);
    tt=sym('tt')
    v(1) = (a(1) + b(1)*tt);  % rotating solution
    v(2:n) = a(2:n).*cos(tt*sqrt(lambda(2:n))) + b(2:n).*sin(tt*sqrt(lambda(2:n)));  % oscillating solution
    v = v(:);
    u = S*v 
    for m = 1:length(t)
        v(1) = (a(1) + b(1)*t(m));  % rotating solution
        v(2:n) = a(2:n).*cos(t(m)*sqrt(lambda(2:n))) + b(2:n).*sin(t(m)*sqrt(lambda(2:n)));  % oscillating solution
        v = v(:);
        u = S*v  ;             %solution u at t(m)
        X = -sin(phi0 + u); Y = cos(phi0 + u);   %positions of the masses at t(m)
        plot(X, Y, 'o','LineWidth',2,'MarkerEdgeColor','k','MarkerFaceColor','k',  'MarkerSize',20)
        rectangle('Position',[-1 -1 2 2],'LineWidth',2,'Curvature',[1, 1]) % actually, this draws a circle
        title(['Normal modes of ',num2str(n),' linear oscillators: mode ',num2str(j),', t = ',num2str(round(t(m)))]);
        getframe;
        
    end

end
