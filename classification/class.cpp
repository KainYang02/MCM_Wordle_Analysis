#include <bits/stdc++.h>

using namespace std;

int main() {
  freopen("cluster.txt", "r", stdin);
  freopen("ouf.txt", "w", stdout);
  vector<pair<string, int>> words;
  string s;
  int id;
  while (cin >> s >> id) {
    words.emplace_back(s, id);
  }
  sort(words.begin(), words.end(), [&] (const pair<string, int>& a, const pair<string, int>& b) {
    return a.second < b.second;
  });
  for (auto p : words) {
    cout << p.first << ' ' << p.second << '\n';
  }
  return 0;
}