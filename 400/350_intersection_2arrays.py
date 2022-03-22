class Solution:
    def intersect(self, nums1, nums2):
        dct1 = {}
        dct2 = {}
        res = []

        for i in nums1:
            if i in dct1:
                dct1[i] += 1
            else:
                dct1[i] = 1

        for i in nums2:
            if i in dct2:
                dct2[i] += 1
            else:
                dct2[i] = 1

        print(dct1)
        print(dct2)

        for i in dct1:
            if i in dct2:
                for j in range(min(dct1[i],dct2[i])):
                    res.append(i)

        return res

s = Solution()

nums1 = [1,2,2,1]
nums2 = [2,2]
print(nums1, nums2)
print("Output: ", s.intersect(nums1, nums2))
print("Expected: ", [2,2])

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(nums1, nums2)
print("Output: ", s.intersect(nums1, nums2))
print("Expected: ", [4,9])

#the order of elements isn't restricted
