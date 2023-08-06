
#include <stdio.h>
/*#define tokens*/
#define X 100
#define Y 200
#define Z 300




0?(1|2)*0		{ printf("X"); return X; }
1?(0|2)*1		{ printf("Y"); return Y; }
2?(1|0)*2		{ printf("Z"); return Z; }



int main()
{
	int token;
	while(token = yylex())
	{
		//printf("%d ", token);
	}
	return 0;
}