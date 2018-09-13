//果蝇投影
#include <iostream>
#include <stdlib.h>
#include <math>
#define expandDim 600
#define selectRandomData 4
#define BINARYCOL 600

using namespace std;

int **matr;
//data/fly

void creatMatr()
{
	int ranNum = 0;
	matr = new float *[expandDim];
	for (int i = 0; i < 300; i++)
	{
		matr[i] = new float[300](0);
	}
	for (int i = 0; i < expandDim; i++)
	{
		int time = 0;
		while(time!=6){
			ranNum = rand() % 300;
			if (matr[i][ranNum]!=0)
			{
				continue;
			}else if (matr[i][ranNum]==0)
			{
				matr[i][j] = 1;
				time++;
			}
		}
	}
}




float* flyProject(float *inVec)
{
	float *outVec = new float[expandDim](0);

	float ele = 0;
	for (int i = 0; i < expandDim; i++)
	{
		for (int j = 0; j < 300; j++)
		{
			ele += matr[i][j] * inVec[j];
		}
		outVec[i] = ele;
		ele = 0;
	}

	return outVec;
}


void creatMatr()
{
	int ranNum = 0;
	matr = new int *[expandDim];
	for (int i = 0; i < expandDim; i++)
	{
		matr[i] = new int[selectRandomData];
		for (int j = 0; j < selectRandomData; j++)
		{
			matr[i][j] = 0;
		}
	}
	for (int i = 0; i < expandDim; i++)
	{
		int time = 0;
		while(time!=selectRandomData){
			ranNum = rand() % 300;
			if (matr[i][ranNum]!=0)
			{
				continue;
			}else if (matr[i][ranNum]==0)
			{
				matr[i][time] = ranNum;
				time++;
			}
		}
	}
}


float* flyProject(float *inVec)
{
	float *outVec = new float[expandDim];
	for (int i = 0; i < expandDim; i++)
	{
		outVec[i] = 0;
	}

	float ele = 0;
	for (int i = 0; i < expandDim; i++)
	{
		for (int j = 0; j < selectRandomData; j++)
		{
			ele += inVec[matr[i][j]];
		}
		outVec[i] = ele;
		ele = 0;
	}

	return outVec;
}


float* binaryTrans(float* afterWta)
{
	int *beforeWta = getLoc(float* afterWta);

	float *beforeBinary = new float[expandDim];
	

	for (int i = 0; i < expandDim; i++)
	{
		if (beforeWta[i]!=0)
		{
			beforeBinary[beforeWta[i]] = 1;
		}
	}
}  









