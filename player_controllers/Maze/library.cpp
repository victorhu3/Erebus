#include "library.h"
#include "iostream"
using namespace std;

//moves sec direction dir
int moveDir(int sec, Orient dir) {
    return sec + addDir[dir];
}

//checks if wall in direction dir for section sec
bool wall(int sec, Orient dir) {
    switch (dir) {
        case enN:
            return Maze[sec].N;
        case enE:
            return Maze[sec].E;
        case enS:
            return Maze[sec].S;
        case enW:
            return Maze[sec].W;
    }
    return 0;
}

//check if wall in that direction or tile already visited 
//i.e. can/should I move there
bool checkMove(int sec, Orient dir) {
    return !(wall(sec, dir) || (sec > 0 && sec < MAZELEN * MAZEWIDTH && Maze[sec].vis));
}