#include <bits/stdc++.h>

using namespace std;

int main(){
    string str;
    printf("Enter the string");
    cin>>str;
    int length = str.length();
    int open[length+1];
    int close[length+1];

    memset(open,0,sizeof(open));
    memset(close,0,sizeof(close));
    open[0] = close[length] = 0;
    if(str[0] == '('){
        open[1] = 1;
    }
    if(str[length-1] == ')'){
        close[length-1] = 1;
    }

    for(int i = 1; i < length; i++){
        if(str[i] == '('){
            open[i+1] = open[i] + 1;
        }else{
            open[i+1] = open[i];
        }
    }

    for(int i = length-2; i >= 0; i--){
        if(str[i] == ')'){
            close[i] = close[i+1] + 1;
        }else{
            close[i] = close[i+1];
        }
    }
    int index = 0;
    if(open[length] == 0)
        index = length;
    else if(close[0] == 0)
        index = 0;
    else{
        for(int i = 0; i <= length; i++){
            if(open[i] == close[i])
                index = i;
        }
    }


    printf("Kth index is %d", index);
}
