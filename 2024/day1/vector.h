#ifndef VECTOR
#define VECTOR

#define SCALING_FACTOR 2
#define BUFFER 500

typedef unsigned int uint;
typedef struct Vector Vector;
typedef struct Vector {
  int *array;
  uint size;
  uint maxSize;
  void (*append)(Vector *, int);
  Vector *(*sort)(Vector *v, int (*sortfunc)(int, int));
  uint (*count)(Vector *, int);
} Vector;

Vector *new_vec();

int lessThan(int a, int b);
int greaterThan(int a, int b);

#endif
