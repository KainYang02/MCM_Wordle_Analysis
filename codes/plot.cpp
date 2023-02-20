#include <bits/stdc++.h>

using namespace std;

struct result
{
	int res[5]; // 0 for green, 1 for yellow, 2 for gray
	bool operator == (const result &a) const
	{
		for(int i = 0; i < 5; ++ i)
			if(res[i] != a.res[i]) return 0;
		return 1;
	}
	bool operator < (const result &a) const
	{
		for(int i = 0; i < 5; ++ i)
			if(res[i] != a.res[i]) return res[i] < a.res[i];
		return false;
	}
	void Get(string guess, string standard)
	{
		bool used[5] = {0, 0, 0, 0, 0};
		// prework
		for(int i = 0; i < 5; ++ i)
			res[i] = 2;
		// get greens
		for(int i = 0; i < 5; ++ i)
			if(guess[i] == standard[i])
				used[i] = 1, res[i] = 0;
		// get yellows
		for(int i = 0; i < 5; ++ i)
			if(res[i])
				for(int j = 0; j < 5; ++ j)
					if(guess[i] == standard[j] && !used[j])
					{
						used[j] = 1, res[i] = 1;
						break;
					}
	}
};

vector<string> words,ori_word;

vector<string> remaining;
vector<double> weight;
map<string, double> freq;

double calc_entropy(string current_guess)
{
	map<result, double> mp;
	double sum = 0;
	for(int i = 0; i < remaining.size(); ++ i)
	{
		result nw; nw.Get(current_guess, remaining[i]);
		mp[nw] += weight[i];
		sum += weight[i];
	}
	double entropy = 0;
	for(auto v : mp)
		entropy += v.second / sum * log(1 / (v.second / sum));
	return entropy;
}

vector<pair<double, string> > res, first_choices;
vector<pair<int, string> > diff_res;
double prob[26] = {0.08857938718662953, 0.017270194986072424, 0.04011142061281337, 0.030083565459610027, 0.10250696378830083, 0.01838440111420613,
0.02841225626740947, 0.03899721448467967, 0.05682451253481894, 0.0022284122562674096, 0.019498607242339833,
0.06239554317548746, 0.03064066852367688, 0.04902506963788301, 0.07409470752089137, 0.03565459610027855,
0.002785515320334262, 0.07409470752089137, 0.04902506963788301, 0.07242339832869081, 0.03565459610027855, 
0.013927576601671309, 0.016713091922005572, 0.0038997214484679664, 0.033983286908077996, 0.002785515320334262};

vector<string> hist_guess;
vector<result> hist_res;

bool hard_mode = true;

int mrand()
{
	int tp = 0;
	for(int i = 0; i < 30; ++ i)
		tp = tp * 2 + rand() % 2;
	return tp;
}

int main()
{
	srand(19491001);
	ifstream freq_input; freq_input.open("frequency.txt");
	ifstream wordlist_input; wordlist_input.open("wordlist_small.txt");
	string tmp;
	while(wordlist_input >> tmp)
	{
		wordlist_input >> tmp;
		wordlist_input >> tmp;
	//	words.push_back(tmp);
		ori_word.push_back(tmp);
		wordlist_input >> tmp;
		wordlist_input >> tmp;
		wordlist_input >> tmp;
		wordlist_input >> tmp;
		wordlist_input >> tmp;
		wordlist_input >> tmp;
		wordlist_input >> tmp;
		wordlist_input >> tmp;
		wordlist_input >> tmp;
	}
	// inject 1000 words
	ifstream wordlelist_full; wordlelist_full.open("wordlist.txt");
	while(wordlelist_full >> tmp)
	{
		tmp.erase(tmp.begin());
		tmp.erase(-- tmp.end());
		tmp.erase(-- tmp.end());
		words.push_back(tmp);
	}
	double minimum = 1e100;
	tmp = "aaaaa";
	while(freq_input >> tmp)
	{
		double freq_word;
		freq_input >> freq_word;
		freq[tmp] = freq_word;
	}
	ofstream json_output; json_output.open("freq.json");
	ifstream clus; clus.open("cluster.txt");
	json_output << "{\n";
	string str;
	while(clus >> str)
	{
		int useless; clus >> useless >> useless;
		double ave = 0;
		for(int i = 1;i <= 7; ++ i)
		{
			clus >> useless;
			ave += i * useless / 100.0;
		}
		json_output << "\t\"" << str << "\": ";
		json_output << "[" << freq[str] << ", " << ave << "],\n";
	}
	json_output << "}\n";
	return 0;
}