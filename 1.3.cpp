#include <bits/stdc++.h>
using namespace std;

string removeDuplicates(string s)
{
    int index = 0, j;

    for (int i = 0; i < s.size(); ++i)
    {
        for (j = 0; j < i; j++)
            if (s[i] == s[j])
                break;

        if (i == j)
            s[index++] = s[i];
    }

    s.resize(index);

    return s;
}

int main()
{
    string s = "saparov";
    s = removeDuplicates(s);
    cout << s;
}