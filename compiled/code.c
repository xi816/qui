#include "stdqui.h"

int nl() {
  stpush(10);
  stemit();
}

int main() {
  stpush(5);
  stpush(6);
  stband();
  stprt();
  nl();
  stpush(9);
  stpush(4);
  stprt();
  nl();
  stpush(5);
  stpush(0);
  stbor();
  stprt();
  nl();
  stpush(0);
  return stpop();
}
