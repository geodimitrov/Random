#include <string>

using namespace std;

string sliceString (string str )
{
  string newStr = str.substr(1, str.length() - 2);
  return newStr;
}