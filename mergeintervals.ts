class Solution:
    def merge(self, intervals):
        intervals.sort()

        // # merge=[]
        // # n=len(intervals)
        // # i=0
        // # while i <n:
        // #     start=intervals[i][0]
        // #     end=intervals[i][1]
        // #     j=i+1
        // #     while j <n and intervals[j][0]<=end:
        // #         end=max(end,intervals[j][1])
                
        // #         j+=1
        // #     merge.append([start,end])
        // #     i=j
        // # return merge
        intervals.sort()
        merge=[]

        for interval in intervals:
            if not  merge or merge[-1][1]<interval[0]:
                merge.append(interval)
            else:
                merge[-1][1]=max(interval[1],merge[-1][1])
        return merge

            
    