function [d_s,v_s] = shark(x,y)
%UNTITLED3 Summary of this function goes here
%   Detailed explanation goes here

beta=atan2(y,x);

if beta < pi
    beta=abs(beta);
end

d_s=beta;

v_s=d_s/4;

end

