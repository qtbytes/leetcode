// Created by none at 2025/05/26 10:50
// leetgo: dev
// https://leetcode.com/problems/logger-rate-limiter/

#include "LC_IO.h"
#include <bits/stdc++.h>
#include <unordered_map>
using namespace std;

// @lc code=begin

class Logger {
public:
  std::unordered_map<string, int> map;

  bool shouldPrintMessage(int timestamp, string message) {
    if (!map.contains(message) || timestamp - map[message] >= 10) {
      map[message] = timestamp;
      return true;
    }
    return false;
  }
};

// @lc code=end

int main() {
  ios_base::sync_with_stdio(false);
  stringstream out_stream;

  vector<string> method_names;
  LeetCodeIO::scan(cin, method_names);

  Logger *obj;
  const unordered_map<string, function<void()>> methods = {
      {"Logger",
       [&]() {
         cin.ignore();
         obj = new Logger();
         out_stream << "null,";
       }},
      {"shouldPrintMessage",
       [&]() {
         int timestamp;
         LeetCodeIO::scan(cin, timestamp);
         cin.ignore();
         string message;
         LeetCodeIO::scan(cin, message);
         cin.ignore();
         LeetCodeIO::print(out_stream,
                           obj->shouldPrintMessage(timestamp, message));
         out_stream << ',';
       }},
  };
  cin >> ws;
  out_stream << '[';
  for (auto &&method_name : method_names) {
    cin.ignore(2);
    methods.at(method_name)();
  }
  cin.ignore();
  out_stream.seekp(-1, ios_base::end);
  out_stream << ']';
  cout << "\noutput: " << out_stream.rdbuf() << endl;

  delete obj;
  return 0;
}
