#include <Stdio.h>
void prime(int n)
{
    int spf[100] = {0};
    for (int i = 2; i <= n; i++)
    {
        spf[i] = i;
    }

    for (int i = 2; i <= n; i++)
    {

        if (spf[i] == i)
        {

            for (int j = i * i; j <= n; j += i)
            {
                if(spf[j]==j){
                    spf[j] = i;
                }
            }
        }
    }
         while(n!=1){
             printf("%d\n",spf[n]);
             n=n/spf[n];
         }
}
int main()
{
    prime(16);

    return 0;
}