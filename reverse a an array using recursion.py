class Solution:
    def reverse(self, arr: list, n: int) -> None:
        def helper (arr, i,j):
            if i>= j :
              return
            arr[i],arr[j]=arr[j],arr[i]
            helper (arr,i+1,j-1)

        helper (arr,0,n-1)
