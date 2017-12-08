#include <bits/stdc++.h>

using namespace std;

int main()
{
    string str = "";
    cin>>str;
    bool valid = false;
    int startIndex, endIndex, length;
    startIndex = endIndex = length = -1;

    for(int i = 0; i < str.length(); i++){
        if(str[i] >= '0' && str[i] <= '9'){
            if((endIndex - startIndex + 1 > length) && valid){
                length = endIndex - startIndex + 1;
            }
            valid = false;
            startIndex = -1;
            endIndex = -1;
        }else{
            if(str[i] >= 'A' && str[i] <= 'Z'){
                valid = true;
            }

            if(startIndex == -1){
                startIndex = i;
            }else{
                endIndex = i;
            }
        }
    }

    if((endIndex - startIndex + 1 > length) && valid){
        length = endIndex - startIndex + 1;
    }
    if(length == -1){
        printf("No valid substring");
    }else
        printf("length %d", length);
}
