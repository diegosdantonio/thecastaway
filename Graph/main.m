clc; clear all; close all;

r = 1;
c = [0 0];
pos = [c-r 2*r 2*r];

%create circle
rectangle('Position',pos,'Curvature',[1 1],'LineWidth',2)
grid on
hold on 
box on
axis equal

for i=1:50000
    [x0,y0]=ramdompoint_test;
    
%      x0=-0.5;
%      y0=-0.5;

     [x,y,d_c,v_c]=costaway(x0,y0);
     [d_s,v_s] = shark(x,y);
    
%    v_c=(1-sqrt(x0^2+y0^2));
%    v_s=abs((atan2(y0,x0))/4);
    
%     captura=v_s-v_c
    captura=v_s-v_c;
    
    if(captura < 0 && captura > -0.01)
            
         plot(x0,y0,'k.')
         hold on  
    end 
    if(captura < -0.01)
        plot(x0,y0,'r*')
        hold on  
    end 
    if(captura > 0)
        plot(x0,y0,'g*')
        hold on  
    end 
end 

legend('Island boundary','Start limit','Safe region','Unsafe region')
