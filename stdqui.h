#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

long long int stack[100];
int sptr = 0;


// Nullary operators
// push values
void stpush(long long int val) {
  stack[sptr] = val;
  sptr++;
}

// integer input
void stintinput() {
  int inp;
  scanf("%d", &inp);
  stack[sptr] = inp;
  sptr++;
}


// Unary operators
// pop the values
long long int stpop() {
  sptr--;
  long long int temp = stack[sptr];
  stack[sptr] = 0;
  return temp;
}

// duplicate the value
void stdup() {
  stack[sptr] = stack[sptr-1];
  sptr++;
}

// not operator
void stbnot() {
  stack[sptr-1] = !stack[sptr-1];
}

// print the value
void stprt() {
  printf("%lld", stack[sptr-1]);
  stack[sptr-1] = 0;
  sptr--;
}

// print the ASCII value
void stemit() {
  printf("%c", stack[sptr-1]);
  stack[sptr-1] = 0;
  sptr--;
}


// Binary operators
// swap two values
void stswap() {
  long long int temp = stack[sptr-2];
  stack[sptr-2] = stack[sptr-1];
  stack[sptr-1] = temp;
}

// add: +
void stadd() {
  stack[sptr-2] += stack[sptr-1];
  sptr--;
}

// sub: -
void stsub() {
  stack[sptr-2] -= stack[sptr-1];
  sptr--;
}

// mul: *
void stmul() {
  stack[sptr-2] *= stack[sptr-1];
  sptr--;
}

// div: // (only truediv now bc' of all in stack is long long int)
void stdiv() {
  stack[sptr-2] /= stack[sptr-1];
  sptr--;
}

// mod: %
void stmod() {
  stack[sptr-2] %= stack[sptr-1];
  sptr--;
}

// eq: ==
void steq() {
  stack[sptr-2] = (int) (stack[sptr-2] == stack[sptr-1]);
  sptr--;
}

// neq: !=
void stneq() {
  stack[sptr-2] = (int) (stack[sptr-2] != stack[sptr-1]);
  sptr--;
}

// gt: >
void stgt() {
  stack[sptr-2] = (int) (stack[sptr-2] > stack[sptr-1]);
  sptr--;
}

// lt: <
void stlt() {
  stack[sptr-2] = (int) (stack[sptr-2] < stack[sptr-1]);
  sptr--;
}

// geq: >=
void stgeq() {
  stack[sptr-2] = (int) (stack[sptr-2] >= stack[sptr-1]);
  sptr--;
}

// leq: <=
void stleq() {
  stack[sptr-2] = (int) (stack[sptr-2] <= stack[sptr-1]);
  sptr--;
}

// band: &
void stband() {
  stack[sptr-2] &= stack[sptr-1];
  sptr--;
}

// bor: |
void stbor() {
  stack[sptr-2] |= stack[sptr-1];
  sptr--;
}

// bxor: ^
void stbxor() {
  stack[sptr-2] ^= stack[sptr-1];
  sptr--;
}
