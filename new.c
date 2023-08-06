%{
#include <stdio.h>
#define IDENTIFIER 10
%}
%%
[a-zA-Z]([a-zA-Z]|[0-9])*       { printf("found IDENTIFIER\n"); return IDENTIFIER; }
%%


int main()
{
	
	int t = yylex();
	printf("first token = %d\n", t);
	return 0;
}