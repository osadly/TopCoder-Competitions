'''
Problem Statement
Given is a S of lowercase English letters ('a'-'z') and an K.

The string S has at least K characters, and none of its last K characters are 'a's.

Your task is to simultaneously shift each 'a' in S by K positions to the right. (The other letters in S must remain in their original relative order.)

Return the resulting string.

Definition
Class: ARight
Method: modify
Parameters: string, integer
Returns: string
Method signature: def modify(self, S, K):
Limits
Time limit (s): 2.000
Memory limit (MB): 256
Constraints
- K will be between 1 and 50, inclusive.
- S will have between K and 100 characters, inclusive.
- Each character in S will be a lowercase English letter ('a'-'z').
- None of the last K characters in S will be 'a'.
Examples
0)
"topcoder"
3
Returns: "topcoder"
No 'a's to move, so the resulting string is the same as the initial one.
1)
"bananas"
1
Returns: "bnanasa"
2)
"aaaaabbbbb"
5
Returns: "bbbbbaaaaa"
3)
"abracadabrahocuspocus"
6
Returns: "brcdbrahoacauaspaocus"
4)
"aardvark"
1
Returns: "raadvrak"
5)
"aardvark"
2
Returns: "rdaavrka"
This problem statement is the exclusive and proprietary property of TopCoder, Inc. Any unauthorized use or reproduction of this information without the prior written consent of TopCoder, Inc. is strictly prohibited. (c)2003, TopCoder, Inc. All rights reserved.
'''
#=================================================
class ARight:
	def modify(self, S, K):
		ret=list('_'*len(S))
		for i in range(len(S)):
			if(S[i]=='a'):
				ret[(i+K)%len(S)]='a'
		
		j=0
		for i in range(len(ret)):
			if ret[i]=='_':
				while(j<len(S) and S[j]=='a'):
					j+=1
				if j<len(S):
					ret[i]=S[j]
					j+=1

		ret2=''.join(ret)
		return ret2