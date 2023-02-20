#include <bits/stdc++.h>

using namespace std;

vector<string> vec;

int main()
{
	string str;
	while(cin >> str)
		vec.push_back(str);
	for(auto v : vec)
		cout << v << ",";
	return 0;
}