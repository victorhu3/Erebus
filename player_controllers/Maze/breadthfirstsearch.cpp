#include <queue>
#include <stack>
#include <iostream>
#include "library.h"
using namespace std;

bool BFS(int sec) {
    int nextSec;
    queue<int> bfsQueue;
    stack<int> path;
    Orient dir = Orientation;
    int parentChild[MAZELEN * MAZEWIDTH];
    bfsQueue.push(sec);
    memset(parentChild, -1, sizeof(parentChild) / sizeof(parentChild[0]));
    
    getSurroundings();

    //traverse maze until find unvisited tile, which will be stored in sec
    while (!Maze[(sec = bfsQueue.front())].vis) {
        bfsQueue.pop();
        for (int x = 0; x < 4; x++) {
            nextSec = moveDir(sec, dir);
            if (parentChild[nextSec] == -1 && !wall(sec, dir)) {
                bfsQueue.push(nextSec);
                parentChild[nextSec] = sec;
            }
            dir++;
        }
        if (bfsQueue.empty)
            return false;
    }

    //push path into stack
    while (parentChild[sec] != -1) {
        path.push(sec);
        sec = parentChild[sec];
    }

    //traverse path
    while (!path.empty()) {
        nextSec = path.top();
        path.pop();
        for (Orient direction = enN; direction < 4; direction++)
            if (nextSec - sec == addDir[direction])
                move(direction);
    }
    
    return true;
}