#include <bits/stdc++.h>
using namespace std;

void reverse(char str[])
{
    int size = 0;

    while (str[size] != '\0')
    {
        size++;
    }

    for(int i = 0; i < size / 2; i++)
    {
        char temp = str[i];
        str[i] = str[size - 1 - i];
        str[size - 1 - i] = temp;
    }    
}

int main()
{
    char str[] = "abcd";

    reverse(str);

    cout << str;
}