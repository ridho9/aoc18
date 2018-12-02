#include "stdio.h"

int main()
{
    char strings[250][30];
    int diff;
    for (int i = 0; i < 250; ++i)
        gets(strings[i]);

    for (int a = 0; a < 249; ++a)
        for (int b = a + 1; b < 250; ++b)
        {
            diff = 0;
            for (int i = 0; i < 27; i++)
                if (strings[a][i] != strings[b][i])
                    diff++;
            if (diff == 1)
            {
                printf("%d\n", diff);
                printf("%s\n", strings[a]);
                printf("%s\n", strings[b]);
                for (int i = 0; i < 27; i++)
                    if (strings[a][i] == strings[b][i])
                        printf("%c", strings[a][i]);
                printf("\n");
                return;
            }
        }
}