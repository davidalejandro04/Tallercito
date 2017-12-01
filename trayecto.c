#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <math.h>

int main()
{

	FILE *punto = fopen("rrt_course.csv", "w");
	fprintf(punto,"x,y,yaw\n");
	double xIn,yIn,yawIn,xAct,yAct,yawAct;
	xIn=0.15;
	yIn=0.15;
	yawIn=0.0;

	double delta=0.05;
	xAct=xIn;
	yAct=yIn;
	yawAct=yawIn;


	fprintf(punto,"%lf,%lf,%lf\n",xIn,yIn,yawIn);
	int i,j;
	j=1;
		while(yAct<=3-yIn)
		{
			xAct=xAct;
			yAct=yAct+delta;
			yawAct=yawAct;
		
			fprintf(punto,"%lf,%lf,%lf\n",xAct,yAct,yawAct);
		}	
		while(xAct<=3-xIn)
		{
			xAct=xAct+delta;
			yAct=yAct;
			yawAct=yawAct;
		
			fprintf(punto,"%lf,%lf,%lf\n",xAct,yAct,yawAct);
		}
		while(yAct>=yIn)
		{
			xAct=xAct;
			yAct=yAct-delta;
			yawAct=yawAct;
		
			fprintf(punto,"%lf,%lf,%lf\n",xAct,yAct,yawAct);
		}


		while(xAct>=3*xIn)
		{
			xAct=xAct-delta;
			yAct=yAct;
			yawAct=yawAct;
		
			fprintf(punto,"%lf,%lf,%lf\n",xAct,yAct,yawAct);
		}	
		while(yAct<=3-3*yIn)
		{
			xAct=xAct;
			yAct=yAct+delta;
			yawAct=yawAct;
		
			fprintf(punto,"%lf,%lf,%lf\n",xAct,yAct,yawAct);
		}	
		while(xAct<=3-3*xIn)
		{
			xAct=xAct+delta;
			yAct=yAct;
			yawAct=yawAct;
		
			fprintf(punto,"%lf,%lf,%lf\n",xAct,yAct,yawAct);
		}
		while(yAct>=3*yIn)
		{
			xAct=xAct;
			yAct=yAct-delta;
			yawAct=yawAct;
		
			fprintf(punto,"%lf,%lf,%lf\n",xAct,yAct,yawAct);
		}
		while(xAct>=5*xIn)
		{
			xAct=xAct-delta;
			yAct=yAct;
			yawAct=yawAct;
		
			fprintf(punto,"%lf,%lf,%lf\n",xAct,yAct,yawAct);
		}
		while(yAct<=3-5*yIn)
		{
			xAct=xAct;
			yAct=yAct+delta;
			yawAct=yawAct;
		
			fprintf(punto,"%lf,%lf,%lf\n",xAct,yAct,yawAct);
		}	
		while(xAct<=3-5*xIn)
		{
			xAct=xAct+delta;
			yAct=yAct;
			yawAct=yawAct;
		
			fprintf(punto,"%lf,%lf,%lf\n",xAct,yAct,yawAct);
		}
		while(yAct>=5*yIn)
		{
			xAct=xAct;
			yAct=yAct-delta;
			yawAct=yawAct;
		
			fprintf(punto,"%lf,%lf,%lf\n",xAct,yAct,yawAct);
		}
		while(xAct>=7*xIn)
		{
			xAct=xAct-delta;
			yAct=yAct;
			yawAct=yawAct;
		
			fprintf(punto,"%lf,%lf,%lf\n",xAct,yAct,yawAct);
		}
		while(yAct<=3-7*yIn)
		{
			xAct=xAct;
			yAct=yAct+delta;
			yawAct=yawAct;
		
			fprintf(punto,"%lf,%lf,%lf\n",xAct,yAct,yawAct);
		}
		while(xAct<=3-7*xIn)
		{
			xAct=xAct+delta;
			yAct=yAct;
			yawAct=yawAct;
		
			fprintf(punto,"%lf,%lf,%lf\n",xAct,yAct,yawAct);
		}
		while(yAct>=7*yIn)
		{
			xAct=xAct;
			yAct=yAct-delta;
			yawAct=yawAct;
		
			fprintf(punto,"%lf,%lf,%lf\n",xAct,yAct,yawAct);
		}
		while(xAct>=9*xIn)
		{
			xAct=xAct-delta;
			yAct=yAct;
			yawAct=yawAct;
		
			fprintf(punto,"%lf,%lf,%lf\n",xAct,yAct,yawAct);
		}
		while(yAct<=3-9*yIn)
		{
			xAct=xAct;
			yAct=yAct+delta;
			yawAct=yawAct;
		
			fprintf(punto,"%lf,%lf,%lf\n",xAct,yAct,yawAct);
		}
		while(xAct<=3-9*xIn)
		{
			xAct=xAct+delta;
			yAct=yAct;
			yawAct=yawAct;
		
			fprintf(punto,"%lf,%lf,%lf\n",xAct,yAct,yawAct);
		}
		while(yAct>=9*yIn)
		{
			xAct=xAct;
			yAct=yAct-delta;
			yawAct=yawAct;
		
			fprintf(punto,"%lf,%lf,%lf\n",xAct,yAct,yawAct);
		}

	


//-----------------------------------------------------//-----------------------------------------------------//-----------------------------------------------------
//-----------------------------------------------------//-----------------------------------------------------//-----------------------------------------------------

}

