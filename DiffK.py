class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        def binary_search(A, target, left, right):
            while left <= right:
                mid = (left + right) // 2
                if A[mid] == target:
                    return 1
                elif A[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return 0
    
        for i in range(len(A) - 1):
            target = A[i] + B
            found = binary_search(A, target, i+1):
            if found:
                return 1
        
        return 0 