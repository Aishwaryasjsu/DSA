class Solution:
    #maintaing order in stack in increasing order 
    def nextLargerElement(self, arr):
        st=[]
        for i in range(len(arr)-1,-1,-1):
            if not st:
                st.append(arr[i])
                arr[i]=-1
            elif st[-1]>arr[i]:
                top=st[-1]
                st.append(arr[i])
                arr[i]=top
                
            else:
                while st and st[-1]<=arr[i]:
                    st.pop()
                if not  st:
                    st.append(arr[i])
                    arr[i]=-1
                else:
                    top=st[-1]
                    st.append(arr[i])
                    arr[i]=top
                            
                            
                          
        return arr

