#include <stdio.h> 
#include <string.h> 

int max(int  num1, int num2, char* name_string){ 
 int max; 
int result;
if(num1 > num2){
if(num1 < 1000){
result = 2000;
}
else {
result = num2;
}
}
else {
result = num1;
}
max = result;

return max;
}

int main(){ 
int a,b,ret;

char c[100];
a = 100;
b = 200;
strcpy(c, "hej");
ret = max(a,b,c);
return 0;
 }