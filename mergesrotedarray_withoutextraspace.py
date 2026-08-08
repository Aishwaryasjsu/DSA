class Solution:
    def merge(self, nums1, m, nums2, n):
        # with EXTRA SPACE # o(m+n) space o(m+n)
        # left=0
        # right=0
        # index=0
        # merge=[0]*(m+n)
        # while left <m and right <n:
        #     if nums1[left]<nums2[right]:
        #         merge[index]=nums1[left]
        #         left+=1
        #     else:
        #         merge[index]=nums2[right]
        #         right+=1
        #     index+=1
        # while left<m:
        #     merge[index]=nums1[left]
        #     left+=1
        #     index+=1
        # while right<n:
        #     merge[index]=nums2[right]
        #     right+=1
        #     index+=1
        # for i in range(m+n):
        #     nums1[i]=merge[i]

        j=n-1
        i=m-1
        ind=m+n-1
        while j>=0:
            if i>=0 and  nums1[i]>nums2[j]:
                nums1[ind]=nums1[i]
                i-=1
                ind-=1
            else:
                nums1[ind]=nums2[j]
                j-=1
                ind-=1




