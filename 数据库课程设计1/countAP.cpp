#include <iostream>
#include <stdlib>
#include <cstring>
using namespace std;

int* KNN;

float AP(int *myKNN, int k)
{
	int truth = 0, total = 0;
	float prec = 0;

	for (int i = 0; i < k; i++)
	{
		total++;

		if (isRealKNN(myKNN[i], k))
		{
			truth++;
			prec += truth / total;
		}
	}
	return prec / k;
}

bool isRealKNN(int tempKNN, int k)
{
	for (int i = 0; i < k; i++)
	{
		if (tempKNN==KNN[i])
		{
			return true;
		}
	}
	return false;
}