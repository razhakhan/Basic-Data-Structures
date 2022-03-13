#User function Template for python3

class Solution:
    
    #Function to find largest rectangular area possible in a given histogram.
    def getMaxArea(self,heights):
        stack = [0]
        heights.append(0)
        ans = 0
        for i in range(1, len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                idx = stack.pop()
                h = heights[idx]
                #w=height of all columns adjacent to each other that are greater than i'th column height ( left and right )
                w = i - stack[-1] - 1 if stack else i
                #area=height of i'th column * possible width
                ans = max(ans, h * w)
            stack.append(i)
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.getMaxArea(a))
# } Driver Code Ends
