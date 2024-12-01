#include "vector.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void resize(Vector *v, uint new_size) {
  v->maxSize = new_size;
  v->array = (int *)realloc(v->array, v->maxSize * sizeof(v->array));
}

void append(Vector *v, int elem) {
  if (v->size + 1 > v->maxSize) {
    resize(v, v->maxSize * SCALING_FACTOR);
  }
  *(v->array + v->size++) = elem;
}

uint count(Vector *right, int elem) {
  uint count = 0;
  for (int i = 0; i < right->size; i++) {
    count += right->array[i] == elem;
  }

  return count;
}

void swap(int *a, int *b) {
  /*
   * swaps the values at two int pointers
   *
   * @param a value a
   * @param b value b
   */

  int temp = *a;
  *a = *b;
  *b = temp;
}

int lessThan(int a, int b) { return a < b; }
int greaterThan(int a, int b) { return a > b; }

int partition(Vector *v, int l, int r, int (*sortfunc)(int, int)) {
  /*
   * helper function for quicksort()
   *
   * @param v vector to be mutated
   * @param l left bound of subvector
   * @param r right bound of subvector
   * @param sortfunc the function to determine order
   * @return pivot
   */

  int pt = l - 1; // current idx
  int temp, pivot = v->array[r];

  for (int i = l; i <= r; i++) { // swap values based on sortfunc
    if ((*sortfunc)(v->array[i], pivot)) {
      pt++;
      swap((v->array + pt), (v->array + i));
    }
  }
  pt++;
  swap((v->array + r), (v->array + pt)); // place pivot in sorted location
  return pt;
}

void quicksort(Vector *v, int l, int r, int (*sortfunc)(int, int)) {
  /*
   * sorting function
   *
   * @param v vector to be mutated
   * @param l left bound of subvector, inclusive
   * @param r right bound of subvector, inclusive
   * @param sortfunc the function to determine ordering
   */

  // recurse until invalid bounds
  if (l >= r) {
    return;
  }

  int pivot = partition(v, l, r, sortfunc);

  quicksort(v, l, pivot - 1, sortfunc);
  quicksort(v, pivot + 1, r, sortfunc);
}

Vector *sort(Vector *v, int (*sortfunc)(int, int)) {
  Vector *copy = (Vector *)malloc(sizeof *copy);
  memcpy(copy, v, sizeof *v);

  quicksort(v, 0, v->size - 1, sortfunc);

  return copy;
}

Vector *new_vec() {
  Vector *v = (Vector *)malloc(sizeof *v);
  v->array = (int *)malloc(sizeof v->array);
  v->size = 0;
  v->maxSize = 1;
  v->append = &append;
  v->sort = &sort;
  v->count = &count;

  return v;
}
