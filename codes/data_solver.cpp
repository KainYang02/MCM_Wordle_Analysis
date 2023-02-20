#include <bits/stdc++.h>

using namespace std;

const int DATA_LINE = 360;

string data[DATA_LINE];
vector<string> datas[DATA_LINE];
double datas_percent[DATA_LINE][7];

int main() {
	fstream origin_data_file("../.archProblem_C_Data_Wordle.csv");
	// assert(origin_data_file); // 是否打开成功
	freopen("standard_oneline.txt", "w", stdout);
	
	for (int i = 0; i < DATA_LINE; i++) {
		getline(origin_data_file, data[i]);
		// cout << data[i] << endl;
		if (i == 0) continue;
		stringstream cur_data(data[i]);
		string str;
		while (getline(cur_data, str, ',')) {
			datas[i].push_back(str);
		}
		assert(datas[i].size() == 12);
		for (auto j : datas[i]) {
			cout << j << " ";
		}
		cout << endl;
		int sum = 0;
		for (int j = 0; j < 7; j++) {
			datas_percent[i][j] = 1.0 * stoi(datas[i][5 + j]);
			sum += datas_percent[i][j];
			// cout << datas_percent[i][j] << " ";
		}
		// cout << ":" << sum << endl;
	}
	return 0;
}