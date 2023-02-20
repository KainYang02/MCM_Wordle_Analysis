#include <bits/stdc++.h>

using namespace std;

ifstream diff_orig;
map<string, int> diff;

int cnt[7];

int main()
{
	diff_orig.open("diff_orig.txt");
	string str;
	while(diff_orig >> str)
	{
		int dif; diff_orig >> dif;
		diff[str] = dif;
	}
	ifstream our; our.open("cluster.txt");
	while(our >> str)
	{
		cnt[diff[str]] ++;
		for(int i = 1;i <= 9; ++ i) our >> str;
	}
	for(int i = 1;i <= 7; ++ i) cerr << cnt[i] << ", ";
}