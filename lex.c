#include <stdio.h>
#include <ctype.h>
#include <assert.h>

#define INSIDE 0
#define OUTSIDE 1

int main()
{
	int c;
	char buff[200];
	int i = 0;
	int state = OUTSIDE;

	while((c = getchar()) != EOF)
	{
		switch (state)
		{
		case OUTSIDE:
			if (!isspace(c))
			{
				buff[i++] = c;
				state = INSIDE;
			}
			break;

		case INSIDE:
			if (isspace(c))
			{
				buff[i] = '\0';
				printf("found word = %s\n", buff);
				i = 0;
				state = OUTSIDE;
			}
			else
			{
				buff[i++] = c;
				state = INSIDE;
			}
			break;
		default:
			assert(0);
			break;
		
							
		
}
}
return 0;
}