#include <stdio.h>

/**
 * main - check the code
 *
 * Return: Always 0.
 */
int main(void)
{
    char a[8][8] = {
        {'T', 'k', 'b', 'q', 'k', 'b', 'k', 'r'},
        {'3', 'p', 'p', 'p', 'p', 'p', 'p', 'p'},
        {'5', ' ', ' ', ' ', ' ', ' ', ' ', ' '},
        {' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '},
        {' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '},
        {' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '},
        {'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'},
        {'R', 'K', 'B', 'Q', 'K', 'B', 'K', 'R'}
    };

	char x[2][4] = {"abg", "def"};

	char *c = "fady";
	printf("pointer fady - %p\n", c);
    printf("printed - %c\n", (*a)[16]);
	printf("normal way - %c\n", (*(a + 2))[0]);
    return (0);
}