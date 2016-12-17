'''
Basis of Attraction with Newton's Root Convergence Method for Cube Roots of Unity
'''

x = -1:0.008:1; y = -1:0.008:1; 
[x0, y0] = meshgrid(x,y); 
n = zeros(size(x0)); 
for k = 1:length(y), 
  for m = 1:length(x), 
    z = x0(k,m) + 1i*y0(k,m); 
    for itr = 1:100, 
      z = z - (z.^3 - 1)./(3*z.^2); 
      if abs(z - 1) < 1e-10, 
        n(k,m) = itr; break, 
      end, 
    end, 
  end, 
end, 

pcolor(x0,y0,n)
