#include <stdio.h>

/*
Read data from dataset and do something you like.
infile : filename of dataset
n      : number of data point to be read
d      : dimension of a data point
*/
void fileIO(const char* infile, const int n, const d) {
	FILE* fin = NULL;
	
	fin = fopen(infile, "r");
	
	double td;
	int ti;
	for (int i = 0; i < n; i++) {

		// read id into ti
		fscanf(fin, "%d", &ti);
		/* do something */
		
		// read data1 to datad
		for (int j = 0; j < d; j++) {
			
			// read one single data into td
			fscanf(fin, "%lf", &td);
			/* do something */
		}
	}
	
	fclose(fin);
}