#include <bits/stdc++.h>

using namespace std;

ifstream cluster_input, diff_input;
ofstream cluster_output;

map<string, double> dif;
vector<double> ave[15], diff[15], sqr[15];

int main()
{
	cluster_input.open("cluster.txt");
	diff_input.open("diff_gd.txt");
	cluster_output.open("graphing_data.txt");
	// Input diff information, collect diff for each problem
	string str;
	while(diff_input >> str)
	{
		double su = 0;
		diff_input >> su;
		dif[str] = su;
	}
	// Input cluster information, collect average data
	while(cluster_input >> str)
	{
		int cate; cluster_input >> cate;
		int useless; cluster_input >> useless;
		diff[cate].push_back(dif[str]);
		double su = 0;
		int seq[8];
		for(int i = 1;i <= 7; ++ i)
		{
			int orid; cluster_input >> orid;
			seq[i] = orid;
			su += orid / 100.0 * i;
		}
		ave[cate].push_back(su);
		double tp = 0;
		for(int i = 1;i <= 7; ++ i)
			tp += seq[i] / 100.0 * (i - su) * (i - su);
		sqr[cate].push_back(tp);
	}
	for(int i = 0; i < 15; ++ i)
		for(int j = 0; j < ave[i].size(); ++ j)
			cluster_output << i << ", ";
	cluster_output << endl;

	for(int i = 0; i < 15; ++ i)
		for(int j = 0; j < ave[i].size(); ++ j)
			cluster_output << diff[i][j] << ", ";
	cluster_output << endl;


	for(int i = 0; i < 15; ++ i)
		for(int j = 0; j < ave[i].size(); ++ j)
			cluster_output << ave[i][j] << ", ";
	cluster_output << endl;

	for(int i = 0; i < 15; ++ i)
		for(int j = 0; j < ave[i].size(); ++ j)
			cluster_output << sqr[i][j] << ", ";
	cluster_output << endl;
}