class Solution:
    def count_NGE(self, arr, indices):

        ans = []


        for idx in indices:

            x = arr[idx]
         
            cnt = 0

            for j in range(idx + 1, len(arr)):

                if arr[j] > x:
                    cnt += 1

      
            ans.append(cnt)

     
        return ans


class Solution:
    def count_NGE(self, arr, indices):

        ans = []


        for idx in indices:

            x = arr[idx]
         
            cnt = 0

            for j in range(idx + 1, len(arr)):

                if arr[j] > x:
                    cnt += 1

      
            ans.append(cnt)

     
        return ans


