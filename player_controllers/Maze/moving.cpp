#include <iostream>
#include "library.h"
using namespace std;

void move(Orient dir) {
    Section = moveDir(Section, dir);
    Orientation = dir;
}