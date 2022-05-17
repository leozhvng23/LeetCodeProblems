"""
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:

string encode(vector<string> strs) {
  // ... your code
  return encoded_string;
}
Machine 2 (receiver) has the function:
vector<string> decode(string s) {
  //... your code
  return strs;
}
So Machine 1 does:

string encoded_string = encode(strs);
and Machine 2 does:

vector<string> strs2 = decode(encoded_string);
strs2 in Machine 2 should be the same as strs in Machine 1.

Implement the encode and decode methods.

You are not allowed to solve the problem using any serialize methods (such as eval).
"""
from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        seperator = '*'
        
        string = ""
        string += seperator
        
        for v in strs:
            string += (str(len(v)) + seperator + v)
        
        return string

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        
        n, strs, seperator = len(s), [], s[0]

        i = 1
        while i < n:
            l = ''
            while s[i] != seperator:
                l += s[i]
                i += 1
            ct = int(l)
            i += 1
            string = s[i:(i+ct)]
            strs.append(string)
            i += ct
            
        return strs


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))