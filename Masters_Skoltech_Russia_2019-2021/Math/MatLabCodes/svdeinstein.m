%% SVD of Einstein. A. Kasimov. Skoltech. MM-EAS F-2019
% press Cmd-Enter to run the script

clear all; close all; clf

m = 312; n = 223;  % image size in pixels
AE = imresize(double(rgb2gray(imread('einstein.tif'))),[m n]); %load and resize image of size mxn

subplot(1,2,1), pcolor(flipud(AE)), shading interp, colormap(gray), axis equal
set(gca,'Xtick',[],'Ytick',[])
title('Full rank approximation of Einstein');
%pause;

[U S V] = svd(AE); 
for k = 1:2:31  % rank-k approximation of Einstein
    AEk = U(:,1:k)*S(1:k,1:k)*V(:,1:k)';
    subplot(1,2,1), pcolor(flipud(AEk)), shading interp, colormap(gray), axis equal
    title(['Rank ',int2str(k),' approximation of Einstein']);
    pause(0.5);  % pause for 0.5 seconds. 
end

% plot the singular values
subplot(1,2,2), loglog(diag(S),'.','MarkerSize',20), axis on, grid on
title 'Singular values'
ylabel '\sigma'
xlabel 'n'

