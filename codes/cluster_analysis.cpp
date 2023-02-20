#include <bits/stdc++.h>

using namespace std;

ifstream cluster_input, diff_input;
ofstream cluster_output, diff_output;

map<string, double> dif;

double minx[15], maxx[15], mean[15], sqr[15];
double ave_minx[15], ave_maxx[15], ave_mean[15], ave_sqr[15];
double ave_sqr2[15];
int cnt[15];
vector<double> val[15], ave_val[15];

int main()
{
	cluster_input.open("cluster.txt");
	diff_input.open("simulate_easymode_gd.txt");
	cluster_output.open("cluster_ana.txt");
	diff_output.open("diff_gd.txt");
	// Input diff information, collect diff for each problem
	for(int i = 0; i < 15; ++ i) minx[i] = ave_minx[i] = 1e100;
	string str;
	while(diff_input >> str)
	{
		int pred;
		double su = 0;
		for(int i = 1; i <= 7; ++ i)
		{
			diff_input >> pred;
			if(i < 7)
				su += pred / 200.0 * i;
			else
				su += pred / 200.0 * i;
		}
		dif[str] = su;
		diff_output << str << " " << dif[str] << endl;
	}
	// Input cluster information, collect average data
	while(cluster_input >> str)
	{
		int cate; cluster_input >> cate;
		int useless; cluster_input >> useless;
		cnt[cate] ++;
		minx[cate] = min(minx[cate], dif[str]);
		maxx[cate] = max(maxx[cate], dif[str]);
		mean[cate] += dif[str];
		double su = 0;
		int seq[8];
		for(int i = 1;i <= 7; ++ i)
		{
			int orid; cluster_input >> orid;
			seq[i] = orid;
			su += orid / 100.0 * i;
		}
		ave_minx[cate] = min(ave_minx[cate], su);
		ave_maxx[cate] = max(ave_maxx[cate], su);
		ave_mean[cate] += su;
		val[cate].push_back(dif[str]);
		ave_val[cate].push_back(su);
		for(int i = 1;i <= 7; ++ i)
			ave_sqr2[cate] += seq[i] / 100.0 * (i - su) * (i - su);
	}
	for(int i = 0; i < 15; ++ i)
	{
		cluster_output << "Cluster #" << i << endl;
		cluster_output << "Ave : ";
		ave_mean[i] /= cnt[i];
		for(auto v : ave_val[i])
			ave_sqr[i] += (v - ave_mean[i]) * (v - ave_mean[i]);
		ave_sqr[i] /= cnt[i];
		mean[i] /= cnt[i];
		for(auto v : val[i])
			sqr[i] += (v - mean[i]) * (v - mean[i]);
		sqr[i] /= cnt[i];
		cluster_output << ave_minx[i] << " " << ave_maxx[i] << " " << ave_mean[i] << " " << ave_sqr[i] << endl;
		cluster_output << "Diff : " << minx[i] << " " << maxx[i] << " " << mean[i] << " " << sqr[i] << endl;
		cluster_output << ave_sqr2[i] / cnt[i] << endl;
	}
}