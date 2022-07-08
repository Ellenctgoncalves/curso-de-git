#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int getJump (int higherLimit, int lesserLimit) {
    int mid = ((higherLimit - lesserLimit)/2) + 1;
    return mid;
}

int main()
{
    int w; // width of the building.
    int h; // height of the building.
    cin >> w >> h; cin.ignore();
    int n; // maximum number of turns before game over.
    cin >> n; cin.ignore();
    int x0;
    int y0;
    cin >> x0 >> y0; cin.ignore();

    int x = x0;
    int y = y0;
    int leftLimit, upperLimit= 0;
    int rightLimit = w - 1;
    int downLimit = h - 1;

    // game loop
    while (n) {
        string bomb_dir;
        cin >> bomb_dir; cin.ignore();

        if (bomb_dir == "U"){
            downLimit = y - 1;
            y-= getJump(downLimit, upperLimit);
        } else if (bomb_dir == "D") {
            upperLimit = y + 1;
            y += getJump(downLimit, upperLimit);
        } else if (bomb_dir == "R") {
            leftLimit = x + 1;
            x += getJump(rightLimit, leftLimit);
        } else if (bomb_dir == "L") {
            rightLimit = x - 1;
            x -= getJump(rightLimit, leftLimit);
        } else if (bomb_dir == "UR") {
            downLimit = y - 1;
            leftLimit = x + 1;
            x += getJump(rightLimit, leftLimit);
            y -= getJump(downLimit, upperLimit);
        } else if (bomb_dir == "UL") {
            downLimit = y - 1;
            rightLimit = x - 1;
            x -= getJump(rightLimit, leftLimit);
            y -= getJump(downLimit, upperLimit);
        } else if (bomb_dir == "DR") {
            upperLimit = y + 1;
            leftLimit = x + 1;
            x += getJump(rightLimit, leftLimit);
            y += getJump(downLimit, upperLimit);
        } else if (bomb_dir == "DL") {
            upperLimit = y + 1;
            rightLimit = x - 1;
            x -= getJump(rightLimit, leftLimit);
            y += getJump(downLimit, upperLimit);
        } else {
            cout << "Wrong command."<< endl;
        }

        cout << x << " "<< y << endl;
    }
}