import math
"""
 Given two sorted arrays nums1 and nums2 of size m and n respectively, 
return the median of the two sorted arrays.

 The overall run time complexity should be O(log (m+n)).
"""
#binary search'e gore kodu degistir.
#

def find_median_sorted_array(nums1, nums2):

    nums1 = []
    nums2 = []
    merged_array = []
    x = 0
    y = 1
    while True:
        nums1.append(x)
        x += 2
        if x > 8:
            break

    while True:
        nums2.append(y)
        y += 2
        if y > 20:
            break

    merged_array = nums1 + nums2
    merged_array.sort()
    total_length = len(merged_array)
    print(merged_array)    
    
    if total_length % 2 == 1:
        index = int((total_length - 1) / 2)
        print("toplam eleman sayisi: ",total_length)
        print("median: ",merged_array[index])
        return merged_array[index]
    
    else:
        index = int(total_length / 2)
        print("toplam eleman sayisi: ",total_length)
        print("median: ",(merged_array[index] + merged_array[index-1]) / 2)
        return (merged_array[index] + merged_array[index-1]) / 2




find_median_sorted_array([], [])

