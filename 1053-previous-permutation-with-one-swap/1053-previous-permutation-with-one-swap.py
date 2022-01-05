class Solution:
    def prevPermOpt1(self, A):
        i = len(A) - 2
        while i >= 0 and A[i] <= A[i+1]:
            i -= 1
        pivot = i
        if i == -1:
            return A
        else:
            pivot_2 = pivot + 1
            pivot_2_value = A[pivot_2]
            for i in range(pivot_2, len(A)):
                if A[i] > pivot_2_value and A[i] < A[pivot]:
                    pivot_2 = i
                    pivot_2_value = A[i]
            A[pivot], A[pivot_2] = A[pivot_2], A[pivot]
        return A
        