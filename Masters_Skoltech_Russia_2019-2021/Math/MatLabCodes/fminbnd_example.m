function fminbnd_example

f = @(x) x.^2.*cos(x); % function to minimize

ezplot(f,[0 10]), grid on
%ezplot(f), grid on

% find the minimum in [3 4] or [-1 1] or [0 5] or [0 10]

[x fval exitflag] = fminbnd(f,8,10) % [3,4] - search interval
