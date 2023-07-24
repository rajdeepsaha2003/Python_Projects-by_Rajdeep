#include<stdio.h>
#include<math.h>
#include<conio.h>

float f(float x)
{
	return (1/(1+x*x));
}

int main()
{
	int i, n;
	float a,b,h,sum=0,result;
	printf("\t\t Result by Trapizoidal Method:");
	printf("\n Enter a,b,n:");
	scanf("%f%f%f",&a,&b,&n);
	
	h=(b-a)/n;
	
	for(i=1; i<=n-1; i++)
	{
	sum=sum+f(a+i*h);
    }
	result=h*(f(a)+f(b)+2*sum)/2;
	printf("\n\t The result is %f",result);
	getch();
}