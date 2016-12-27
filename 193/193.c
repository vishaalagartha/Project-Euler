#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

#define MAX 33554432

int main()
{
    int *mu = malloc(sizeof(int)*(MAX+1));
    int i, j;
    #pragma omp parallel for
    for(i=1; i<=MAX; i++)
        mu[i]=1;
    #pragma omp parallel for
    for (i = 2; i <= MAX; i++)
    {
        if (mu[i] == 1)
        {
            for (j = i; j <= MAX; j += i)
                mu[j] *= -i;
            for (j = i * i; j <= MAX; j += i * i)
                mu[j] = 0;
        }
    }
    #pragma omp parallel for
    for (i = 2; i <=MAX; i++)
    {
        if (mu[i] == i)
            mu[i] = 1;
        else if (mu[i] == -i)
            mu[i] = -1;
        else if (mu[i] < 0)
            mu[i] = 1;
        else if (mu[i] > 0)
            mu[i] = -1;
    }



}   
