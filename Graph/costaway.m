function [x,y,d_c,v_c] = costaway(x0,y0)

theta=atan2(y0,x0);

x=cos(theta);
y=sin(theta);

d_c=1-sqrt(x0^2+y0^2);

v_c=d_c/1;

end

