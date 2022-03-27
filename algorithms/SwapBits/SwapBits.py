#User function Template for python3

class Solution:
    def swapBits(self, X, P1, P2, N):
        
        rightmost_side_set1 =  (X >> P1) & ((1<< N) - 1) 
        rightmost_side_set2 =  (X >> P2) & ((1 << N) - 1) 
        xor = (rightmost_side_set1 ^ rightmost_side_set2) 
        xor = (xor << P1) | (xor << P2) 
        answer = X ^ xor 
       
        return answer 



#{ 
#  Driver Code Starts

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        obj = Solution()
        X, P1, P2, N = map(int, input().split())
        print(obj.swapBits(X, P1, P2, N))
        

# } Driver Code Ends