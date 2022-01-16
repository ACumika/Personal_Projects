%% Skoltech, Term 1B-2, 2019. Mathematical Methods in Engineering and Applied Science.
% By Prof. Aslan Kasimov.

%% Unit circle and its transformation
% Press Cmd-Enter to run the cell

clear all, clf

t = linspace(0,2*pi,100); %angle
x = cos(t); y = sin(t)    %rows

subplot(1,2,1), plot(x,y,'-k','LineWidth',2)
axis(3*[-1 1 -1 1]), axis square, grid on

A = [2 1; 1 2]; 
B = A*[x; y];   % the same points transformed by A
u = B(1,:);
v = B(2,:);

subplot(1,2,2), plot(u,v,'-k','LineWidth',2)
axis(3*[-1 1 -1 1]), axis square, grid on


%% Transformation of a sphere 
% 
clear all, clf

n = 100;
[X Y Z] = sphere(n);  %X,Y,Z are n+1 by n+1 matrices of points on the sphere

subplot(1,2,1), surf(X,Y,Z), shading interp, colormap gray
axis square

% we can choose a matrix based on specific eignevalues and eigenvectors
 s1 = [1 0 0]; 
 s2 = [0 1 1]/sqrt(2); 
 s3 = [0 -1 1]/sqrt(2); %orthonormal e-vectors
 A = 4*s1'*s1 + 2*s2'*s2 + 1*s3'*s3; % the matrix with those e-vectors and ane e-values 4,2,1 
%

% or choose any
% A = [ 2 1 0; 1 3 1; 4 2 10]; % we will transform the sphere with this matrix

% [U V W] will be transformed points 
U = X;
V = Y;
W = Z;

for i=1:n+1
    for j=1:n+1
        b = A*[X(i,j) Y(i,j) Z(i,j)]'; %transformed point
        U(i,j) = b(1);
        V(i,j) = b(2);
        W(i,j) = b(3);
    end 
end 

subplot(1,2,2), surf(U,V,W), shading interp, colormap gray %ellipsoid
axis square

%% Iterative solution of linear systems
% will use Jacobi and Gauss-Seidel
clear all; 

A = [2 1 1; 1 2 -2; 0 -1 2] %will converge 
%A = [1 2 -2; 2 1 1; 0 -1 2] %will not converge 
b = [1 1 1]';

if rank(A)<3
    disp('singular matrix')
    return
end

solver  = 'gs'; % 'jac' or 'gs'

x_exact = A\b
tol = 10^-6;
x = [1 1 1]'; %initial guess
err = 1; count = 0;

switch solver 

case 'jac' %Jacobi
    D = diag(diag(A));
    A2 = A - D;
    while err > tol
        b1 = b - A2*x;
        x = D\b1;
        err = norm(x-x_exact);
        %pause
        if err > 100
            break
        end
        count = count +1;
    end
    disp (['iterations ',num2str(count),', err = ',num2str(err)])

case 'gs' % Gauss-Seidel
    A1  = tril(A); %lower triangular part of A including diagonal
    A2 = A - A1;
    while err > tol
        b1 = b - A2*x;
        x = A1\b1;
        err = norm(x-x_exact);
        %pause
        if err > 100
            break
        end
        count = count +1;
    end
    disp (['iterations ',num2str(count),', err = ',num2str(err)])  
    
    otherwise
    disp 'another case'

end
