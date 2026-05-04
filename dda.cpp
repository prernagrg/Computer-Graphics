#include <graphics.h>
#include<iostream>
using namespace std;
int DDA(int,int,int,int);

int DDA(int x1, int y1, int x2, int y2) {
    int dx, dy, steps, k;
    float x, y, xinc, yinc;

    dx = x2 - x1; 
    dy = y2 - y1;

    if (abs(dx) > abs(dy))
        steps = abs(dx);
    else
        steps = abs(dy);

    xinc = (float)dx / steps;
    yinc = (float)dy / steps;

    x = x1;
    y = y1;

    putpixel(x, y, BLUE);

    for (k = 0; k < steps; k++) {
        x = x + xinc;
        y = y + yinc;
        putpixel((int)(x + 0.5), (int)(y + 0.5), WHITE);
        delay(10); // to visualize line drawing slowly
    }
    return 0;
}
int main(int argc, char const *argv[]) 
{

    int gd=DETECT,gm;
     // Initialize graphics
    initgraph(&gd, &gm, (char*)"");
    
    int x1, y1, x2, y2;
    printf("Enter x1 and y1: ");
    scanf("%d%d", &x1, &y1);

    printf("Enter x2 and y2: ");
    scanf("%d%d", &x2, &y2);

    DDA(x1, y1, x2, y2);

    getch();
    closegraph();
    return 0;
}
