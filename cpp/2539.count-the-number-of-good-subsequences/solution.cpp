// Created by none at 2025/05/26 13:11
// leetgo: dev
// https://leetcode.com/problems/count-the-number-of-good-subsequences/

#include "LC_IO.h"
#include <bits/stdc++.h>
#include <print>
#include <unordered_set>
#include <vector>
using namespace std;

// @lc code=begin

int pow(int a, int b, int n) {
  long long x = 1, y = a;
  while (b > 0) {
    if (b % 2 == 1) {
      x = (x * y) % n; // multiplying with base
    }
    y = (y * y) % n; // squaring the base
    b /= 2;
  }
  return x % n;
}

const int MOD = 1e9 + 7;

class Solution {
public:
  int countGoodSubsequences(string s) {
    vector<int> cnt(26, 0);
    int max = 0;
    for (auto &ch : s) {
      cnt[ch - 'a']++;
      max = std::max(max, cnt[ch - 'a']);
    }

    int res = 0;
    vector<long long> f(max + 1, 1);
    unordered_set<int> seen;
    for (int n = 0; n < max; n++) {
      long long cur = 1;
      seen.clear();
      for (auto m : cnt) {
        if (m > n) {
          if (!seen.contains(m)) {
            // comb(m,n+1) = comb(m,n) * (m-n) / (n+1)
            f[m] = f[m] * (m - n) % MOD * pow(n + 1, MOD - 2, MOD) % MOD;
            seen.insert(m);
          }
          cur = cur * (f[m] + 1) % MOD; // comb(m, n)
        }
      }
      res = (res + cur - 1) % MOD;
    }
    return res;
  }
};

// @lc code=end

int main() {
  ios_base::sync_with_stdio(false);
  stringstream out_stream;

  string s;
  LeetCodeIO::scan(cin, s);

  Solution *obj = new Solution();
  auto res = obj->countGoodSubsequences(s);
  LeetCodeIO::print(out_stream, res);
  cout << "\noutput: " << out_stream.rdbuf() << endl;

  delete obj;
  return 0;
}
