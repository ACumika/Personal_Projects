function genetic_example
%Based on Kutz
% fminsearch gives c = [14.6, 0.21, 63.0]

clear all

x = 1:24;
y = [75 77 76 73 69 68 63 59 57 55 54 52 50 ...
     50 49 49 49 50 54 56 59 63 67 72];

subplot(2,1,1), plot(x,y,'ko')
grid on

%pause 
 
xx=1:0.01:24;

m = 500; % number of generations, try also 2000
n = 50; % number of trials,                try 200
n2= 10; % number of trials to be kept,   this must be n/5, try 40 
A = 20+randn(n,1);    %12
B = 1+randn(n,1);     %pi/12
C = 60+randn(n,1);    %60
 
 for jgen=1:m
     
     for j=1:n  % evaluate objective function
         E(j)= sum((A(j)*cos(B(j)*x) + C(j) - y).^2);
     end
     
     [Es,Ej]=sort(E);  % sort from small to large
     
     Ak1=A(Ej(1:n2)); % best 10 solutions
     Bk1=B(Ej(1:n2));
     Ck1=C(Ej(1:n2));
     
     Ak2=Ak1+randn(n2,1)/jgen; % 10 new mutations
     Bk2=Bk1+randn(n2,1)/jgen;
     Ck2=Ck1+randn(n2,1)/jgen;
     
     Ak3=Ak1+randn(n2,1)/jgen; % 10 new mutations
     Bk3=Bk1+randn(n2,1)/jgen;
     Ck3=Ck1+randn(n2,1)/jgen;
     
     Ak4=Ak1+randn(n2,1)/jgen; % 10 new mutations
     Bk4=Bk1+randn(n2,1)/jgen;
     Ck4=Ck1+randn(n2,1)/jgen;
     
     Ak5=Ak1+randn(n2,1)/jgen; % 10 new mutations
     Bk5=Bk1+randn(n2,1)/jgen;
     Ck5=Ck1+randn(n2,1)/jgen;
     
     A=[Ak1; Ak2; Ak3; Ak4; Ak5]; % group new 50
     B=[Bk1; Bk2; Bk3; Bk4; Bk5];
     C=[Ck1; Ck2; Ck3; Ck4; Ck5];
     
     yfit = A(1)*cos(B(1)*xx) + C(1);
     subplot(2,1,1), plot(x,y,'ko',xx,yfit,'k-'); grid on
     subplot(2,1,2), semilogy(abs([A,B,C]),'o')
     drawnow  
     disp(['A=',num2str(A(1)),', B=',num2str(B(1)),', C=',num2str(C(1))])
     %pause

 end

end
