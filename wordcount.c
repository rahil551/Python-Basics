#include <stdio.h>
#include <ctype.h>
#include <assert.h>


#define INSIDE 0
#define OUTSIDE 1


int main()
{
	int c;
	char buf[200];
	int i = 0;
	int state = OUTSIDE;
	
	while ((c = getchar()) != EOF) {
		
		switch(state) {
			case OUTSIDE:
				if (!isspace(c)) {
					buf[i++] = c;
					state = INSIDE;
				}
			break;
			case INSIDE:
				if (isspace(c)) {
					buf[i] = '\0';
					printf("Found word = %s\n", buf);
					i = 0;
					state = OUTSIDE;
					
				} else { /*not space */
					buf[i++] = c;
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