#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv) {
  // use cmd arg argument
  char *filename = "input.txt";
  if (argc > 1) {
    filename = argv[1];
  }

  FILE *f = fopen(filename, "r");

  fclose(f);
  return 0;
}
