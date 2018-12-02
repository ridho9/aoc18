#include "stdio.h"
#include "string.h"

int main()
{
    char line[30];
    int count2 = 0;
    int count3 = 0;
    char have2 = 0;
    char have3 = 0;
    char set[26];

    while (gets(line) > 0)
    {
        have2 = 0;
        have3 = 0;
        memset(set, 0, 26);
        for (char i = 0; i < 26; i++)
        {
            set[line[i] - 'a'] += 1;
        }
        for (char i = 0; i < 26; i++)
        {
            if (set[i] == 2)
                have2 = 1;
            if (set[i] == 3)
                have3 = 1;
        }
        count2 += have2;
        count3 += have3;
    }
    printf("%d\n", count2 * count3);
}