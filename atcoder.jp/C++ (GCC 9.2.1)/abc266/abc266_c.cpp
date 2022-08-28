#include <iostream>
using namespace std;


bool in_triangle(int Ax, int Ay, int Bx, int By, int Cx, int Cy, int Px, int Py) {
    int c1 = (Bx - Ax) * (Py - Ay) - (By - Ay) * (Px - Ax);
    int c2 = (Cx - Bx) * (Py - By) - (Cy - By) * (Px - Bx);
    int c3 = (Ax - Cx) * (Py - Cy) - (Ay - Cy) * (Px - Cx);
    return c1 >= 0 && c2 >= 0 && c3 >= 0 || c1 <= 0 && c2 <= 0 && c3 <= 0;
}


int main()
{
    int Ax, Ay, Bx, By, Cx, Cy, Dx, Dy;
    cin >> Ax >> Ay >> Bx >> By >> Cx >> Cy >> Dx >> Dy;
    
    if (in_triangle(Ax, Ay, Bx, By, Cx, Cy, Dx, Dy) ||
        in_triangle(Ax, Ay, Bx, By, Dx, Dy, Cx, Cy) ||
        in_triangle(Cx, Cy, Dx, Dy, Ax, Ay, Bx, By) ||
        in_triangle(Cx, Cy, Dx, Dy, Bx, By, Ax, Ay)) {
        cout << "No" << endl;
    } else {
        cout << "Yes" << endl;
    }

    return 0;
}