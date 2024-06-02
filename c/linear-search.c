#include <stdio.h>
#define N 6

void find(int item, int size, int array[]);

int main(void)
{
	int array[N] = {1, 2, 3, 4, 5, 6};
	find(5, N, array);
	return 0;
}


void find(int item, int size, int array[])
{
	for (int i=0; i<size; i++)
	{
		if (array[i]==item)
		{
			printf("%i\n", i);
		}
	}
}
