#include "vector.h"
#include <stdio.h>
#include <stdlib.h>

int part1(Vector *left, Vector *right) {
  Vector *sortedLeft = left->sort(left, lessThan);
  Vector *sortedRight = right->sort(right, lessThan);

  int diff = 0, sum = 0;
  for (int i = 0; i < sortedLeft->size; i++) {
    sum += abs(sortedLeft->array[i] - sortedRight->array[i]);
  }

  return sum;
}

int part2(Vector *left, Vector *right) {
  int item, sum = 0;
  for (int i = 0; i < left->size; i++) {
    item = left->array[i];
    sum += right->count(right, item) * item;
  }

  return sum;
}

int main(int argc, char **argv) {
  // use cmd arg argument
  char *filename = "input.txt";
  if (argc > 1) {
    filename = argv[1];
  }

  FILE *f = fopen(filename, "r");
  if (f == NULL) {
    printf("Error reading %s.\n", filename);
    return 1;
  }

  Vector *left = new_vec();
  Vector *right = new_vec();

  int n_left, n_right;
  char buffer[BUFFER];
  while (fgets(buffer, BUFFER, f)) {
    sscanf(buffer, "%d   %d", &n_left, &n_right);

    left->append(left, n_left);
    right->append(right, n_right);
  }

  printf("%d\n", part1(left, right));
  printf("%d\n", part2(left, right));

  return 0;
}
