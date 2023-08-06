
#include <stdio.h>
#include <ctype.h>

// Enumerated types in C

enum token_t { PLUS=0, MINUS, MUL, SEMICOLON, NUMBER, IDENTIFIER, END };

// Represent token table as array

const char * token_table[7] = { "PLUS", "MINUS", "MUL", "SEMICOLON", "NUMBER", "IDENTIFIER", "END" };

int lexer()
{
	int c;
	int state = 0; //0 is the initial state

	while ((c = getchar()) != EOF) {  //step1: outer while loop
	
		switch(state) { // step 2: switch(state) construct

			case 0: //initial state
				switch(c) {
				case '+': state = 1; break;
				case '-': state = 2; break;
				case '*': state = 3; break;
				case ';': state = 4; break;
				case ' ': case '\t': case '\n': /*whitespace*/ state = 0; break;
				default:
					if (isdigit(c)) {
						state = 5;
					} else {
						printf("error near %c\n", c);
						state = 0;
					}
				break;
				}

			break;

			case 1:  ungetc(c, stdin); return PLUS; break;
			case 2:  ungetc(c, stdin); return MINUS; break;
			case 3:  ungetc(c, stdin); return MUL; break;
			case 4:  ungetc(c, stdin); return SEMICOLON; break;
			case 5:
				if (isdigit(c)) {
					state = 5;
				} else {
					state = 6;
				}
			case 6:
				return NUMBER;
				break;
			break;

		} //end switch(state)
	} // end while
	return END;
}
			
int main()
{
	int token = END;
	while ((token = lexer()) != END) {
		printf("token = %d %s\n", token, token_table[token]);
	} 
}
