#include <bits/stdc++.h>

using namespace std;

int main(){
    printf("Enter A and B");
    int a,b,c,d = 0;
    scanf("%d%d", &a, &b);
    c = a*b;

    while(c){
        if(c%2 == 1){
            d++;
        }
        c = c/2;
    }

    printf("Number of set bits are %d", d);
}
