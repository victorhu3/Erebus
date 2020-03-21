#pragma once

#define MAZELEN 8
#define MAZEWIDTH 4
#define up(i) (i - MAZELEN)
#define right(i) (i + 1)
#define down(i) (i + MAZELEN)
#define left(i) (i - 1)

typedef struct{
    bool vis : 1;
    bool N : 1;
    bool E : 1;
    bool S : 1;
    bool W : 1;
} Tile;

enum Orient { enN, enE, enS, enW };
Orient operator++(Orient &obj, int) {
	obj = (Orient)(((int)obj + 1) % 4);
	return obj;
}

extern int Section, StartSection;
extern Tile Maze[MAZELEN * MAZEWIDTH];
extern Orient Orientation;

int addDir[4] = { -MAZELEN, 1, MAZELEN, -1 };

int moveDir(int, Orient);
bool wall(int, Orient);
void move(Orient);
void getSurroundings();
bool BFS(int);