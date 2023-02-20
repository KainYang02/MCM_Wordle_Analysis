#include <bits/stdc++.h>

using namespace std;

map<string, double> ori_diff;
map<string, double> ori_entro;
map<string, double> prob;

double prob_raw[26] = {0.08857938718662953, 0.017270194986072424, 0.04011142061281337, 0.030083565459610027, 0.10250696378830083, 0.01838440111420613,
0.02841225626740947, 0.03899721448467967, 0.05682451253481894, 0.0022284122562674096, 0.019498607242339833,
0.06239554317548746, 0.03064066852367688, 0.04902506963788301, 0.07409470752089137, 0.03565459610027855,
0.002785515320334262, 0.07409470752089137, 0.04902506963788301, 0.07242339832869081, 0.03565459610027855, 
0.013927576601671309, 0.016713091922005572, 0.0038997214484679664, 0.033983286908077996, 0.002785515320334262};

/*
basic score : diff;
entro [-0.33, 0.33]
prob [-0.12, 0.12]
rep [-0.1, 0.1]
*/

vector<pair<double, string> > res;

int main()
{
	ifstream diff_input, entro_input;
	diff_input.open("simulate_easymode_full.txt");
	entro_input.open("wordlist_small.txt");
	string str;
	ofstream dif_output; dif_output.open("diff_sim_small.txt");
	while(diff_input >> str)
	{
		string useless;
		entro_input >> useless >> useless >> useless >> useless >> useless;
		dif_output << str << " ";
		double judge = 0;
		int sum = 0;
		for(int i = 1;i <= 7; ++ i)
		{
			int cn; diff_input >> cn;
			int cn2; entro_input >> cn2;
			judge += cn / 200.0 * i;
		}
		dif_output << judge << endl;
	}
	return 0;
}