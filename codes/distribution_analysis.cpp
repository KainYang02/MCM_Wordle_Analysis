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
		freq[tmp] = (log(freq_word + pow(2, -25)) + 26) * (log(freq_word + pow(2, -25)) + 26);
	}
	for(auto v : words)
		weight.push_back(freq[v]), remaining.push_back(v);
	ofstream entropy_output; entropy_output.open("simulate_easymode.txt");
/*
	for(auto v : ori_word)
		res.push_back(make_pair(calc_entropy(v), v));
	sort(res.begin(), res.end());
	for(auto v : res)
		entropy_output << v.second << " " << v.first << endl;
*/
	for(auto word : freq)
		res.push_back(make_pair(calc_entropy(word.first), word.first));
	sort(res.begin(), res.end());
	reverse(res.begin(), res.end());
	for(auto v : res) first_choices.push_back(v), cerr << v.second << endl;
	result full_correct; full_correct.Get(ori_word[0], ori_word[0]);
/*
5% - smartest
15% - 0.1
15% - 0.2
15% - 0.3
15% - 0.4
15% - 0.5
15% - 0.75
5% - 1.0
*/
	double decision_lis[8] = {0.07, 0.11, 0.14, 0.18, 0.18, 0.14, 0.11, 0.07};
	double range_lis[8] = {0.0, 0.05, 0.1, 0.25, 0.375, 0.5, 0.75, 1.0};
	int bot = 0;
	bool flg = 0;
	for(auto u : ori_word)
	{
	//	flg |= u == "solar";
	//	if(!flg) continue;
		int resu[8] = {0};
		for(int attempt = 200; attempt; -- attempt)
		{
			bot ++;
			double current = attempt / 200.0;
			double ths = 1.0;
			for(int i = 0; i < 8; ++ i)
			{
				current -= decision_lis[i];
				if(current <= 0)
				{
					ths = range_lis[i];
					break;
				}
			}
			weight.clear(); remaining.clear();
			for(auto v : words)
				weight.push_back(freq[v]), remaining.push_back(v);
			int label = first_choices.size() * ths;
			if(!label) ++ label;
			string first_guess;
			if(attempt & 0)
				first_guess = first_choices[mrand() % label].second;
			else
			{
				double su = 0;
				for(int i = 0; i < label; ++ i) su += first_choices[i].first;
				double sed = mrand() % 10000001 / 10000000.0 * su;
				for(int i = 0; i < label; ++ i)
				{
					sed -= first_choices[i].first;
					if(sed <= 0)
					{
						first_guess = first_choices[i].second;
						break;
					}
				}
			}
			result first_res; first_res.Get(first_guess, u);
			hist_res.clear(); hist_guess.clear();
			hist_guess.push_back(first_guess); hist_res.push_back(first_res);
			int diff = 0;
			while(weight.size() > 1)
			{
				res.clear();
				for(int i = weight.size() - 1; i >= 0; -- i)
				{
					result this_res; this_res.Get(hist_guess[diff], remaining[i]);
					if(this_res == hist_res[diff]) continue;
					remaining.erase(remaining.begin() + i); weight.erase(weight.begin() + i);
				}
				diff ++;
				if(diff >= 7) break;
				if(weight.size() == 1) break;
				for(auto word : freq)
				{
					if(!hard_mode)
						res.push_back(make_pair(calc_entropy(word.first), word.first));
					else
					{
						bool flg = 1;
						for(int i = 0; i < diff; ++ i)
						{
							result chk_vali; chk_vali.Get(word.first, hist_guess[i]);
							int cn[26] = {0}, cn2[26] = {0};
							for(int j = 0; j < 5; ++ j)
								if(hist_res[i].res[j] < 2)
								{
									cn2[word.first[j] - 'a'] ++;
									if(!hist_res[i].res[j])
										flg &= chk_vali.res[j] == 0;
									cn[hist_guess[i][j] - 'a'] ++;
								}
								else cn2[word.first[j] - 'a'] ++;
							for(int j = 0; j < 26; ++ j)
								flg &= cn2[j] >= cn[j];
						}
						if(flg)
							res.push_back(make_pair(calc_entropy(word.first), word.first));
					}
				}
				sort(res.begin(), res.end());
				reverse(res.begin(), res.end());
				int label = res.size() * ths;
				if(label == 0) label ++;
				string this_guess;
				if(attempt & 0)
					this_guess = res[mrand() % label].second;
				else
				{
					double su = 0;
					for(int i = 0; i < label; ++ i) su += res[i].first;
					double sed = mrand() % 10000001 / 10000000.0 * su;
					for(int i = 0; i < label; ++ i)
					{
						sed -= res[i].first;
						if(sed <= 0)
						{
							this_guess = res[i].second;
							break;
						}
					}
				}
				result this_res; this_res.Get(this_guess, u);
				hist_guess.push_back(this_guess); hist_res.push_back(this_res);
			}
			diff += 1 - ((*(-- hist_res.end())) == full_correct);
			if(diff > 7) diff = 7;
			resu[diff] ++;
			cerr << bot * 0.5 / ori_word.size() << "%" << endl;
		}
		entropy_output << u << endl;
		for(int i = 1; i <= 7; ++ i)
			entropy_output << resu[i] << endl;
		entropy_output << endl;
		
	}
	sort(diff_res.begin(), diff_res.end());
	for(auto v : diff_res)
		entropy_output << v.second << " " << v.first << endl;
	return 0;
}