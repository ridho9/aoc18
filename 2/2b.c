#include "stdio.h"

#define LINES 50000

int main()
{
    char strings[LINES][30];
    int diff;
    for (int i = 0; i < LINES; ++i)
    {
        gets(strings[i]);
    }

    for (int a = 0; a < LINES - 1; ++a)
        for (int b = a + 1; b < LINES; ++b)
        {
            diff = 0;
            for (int i = 0; i < 27; i++)
                if (strings[a][i] != strings[b][i])
                    diff++;
            if (diff == 1)
            {
                for (int i = 0; i < 27; i++)
                    if (strings[a][i] == strings[b][i])
                        printf("%c", strings[a][i]);
                printf("\n");
                return;
            }
        }
}