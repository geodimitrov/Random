function isPalindrome(string) {
  let revString = string.split('').reverse().join('')

  if (revString.toLowerCase() == string.toLowerCase())
      return true;
  else
      return false;
