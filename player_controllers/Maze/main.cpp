#include "library.h"
#include <iostream>
using namespace std;

Tile Maze[MAZELEN * MAZEWIDTH];
Orient Orientation = enN;
int Section = (MAZELEN / 2 - 1) * MAZEWIDTH + MAZEWIDTH / 2;

int main() {
    int startSection = Section;
    while (BFS(Section));
    Maze[startSection].vis = 0;
    BFS(Section);
}