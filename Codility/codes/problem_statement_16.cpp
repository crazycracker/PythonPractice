#include <bits/stdc++.h>

using namespace std;

int main(){
    int n;
    cout<<"enter the number"<<endl;
    cin>>n;

    int arr[32];

    memset(arr,0,sizeof(arr));
    int i = 0,c = 0;
    while(n){
        if(n%2 == 1){
            arr[i] = 1;
        }
        i++;
        n = n/2;
        c++;
    }
    int maxPeriod = 0;
    for(int p = 1; p <= c/2; p++){
        int k = 0;
        for(;k < c-p; k++){
            if(arr[k] != arr[k+p])
                break;
        }

        if(k == c-p)
            maxPeriod = p;
    }

    cout<<"period is "<<maxPeriod<<endl;
}
