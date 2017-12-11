#include <bits/stdc++.h>

using namespace std;

int solution(vector<int> vec){
    int max_length, length;
    max_length = length = 0;

    int even, odd;
    even = vec[0];
    odd = vec[1];
    length = 2;

    for(int i = 2; i < vec.size();){
        if(even == vec[i]){
            if(odd == vec[i+1]){
                length += 2;
                i += 2;
            }else{
                even = odd;
                odd = vec[i];
                i++;
                length++;
            }
        }else{
            even = odd;
            odd = vec[i];
            i++;
            length = 2;
        }

        if(max_length < length)
            max_length = length;
    }
    // 5 4 -3 4 -3 5 -3 5
    if(max_length == 2)
        max_length = 0;
    return max_length;
}
int main(){
    int n;
    cin>>n;

    vector<int> vec;
    for(int i = 0; i < n; i++)
    {
        int number;
        cin>>number;
        vec.push_back(number);
    }

    cout<<solution(vec);
}
