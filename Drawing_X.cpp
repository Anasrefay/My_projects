#include<iostream>
using namespace std;
int main(){
int N;
cin>>N;
for(int j = 0; j < N; j++){
for(int i = 0; i < N; i++){
if(j != N/2){
if(j == i){
cout<<'\\';
}
else if(i == N - 1 - j){
cout<<'/';
}
else{
cout<<'*';
}
}
else if(j == N/2){
if(i == N/2){
cout<<'X';
}
else{
cout<<'*';
}
}
}
cout<<'\n';
}
}