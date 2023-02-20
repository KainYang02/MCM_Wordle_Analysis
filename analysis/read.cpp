#include <bits/stdc++.h>

using namespace std;

int main() {
  freopen("class4.txt", "r", stdin);
  string word;
  int x[7], xp, xe;
  double y[7] = {0}, yp = 0;
  int counter = 0;
  while (cin >> word) {
    ++counter;
    cin >> xe >> xe;
    for (int i = 1; i <= 6; ++i) {
      cin >> x[i];
      y[i] += x[i];
    }
    cin >> xp;
    yp += xp;
  }
  cerr << counter << '\n';
  for (int i = 1; i <= 6; ++i) {
    y[i] /= counter;
  }
  yp /= counter;
  for (int i = 1; i <= 6; ++i) {
    cout << y[i] << '\n';
  }
  cout << yp << '\n';
}