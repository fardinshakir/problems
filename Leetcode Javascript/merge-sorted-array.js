var merge = function(nums1, m, nums2, n) {
    nums1 = nums1.filter(n => n !=0)
    nums2 = nums2.filter(n => n !=0)
    if (nums1 === undefined || nums1.length == 0 || nums2 === undefined || nums2.length == 0 ) {
        return []
    } else {
        let new_array = []
        while (new_array.length() != m+n -1) {
            
        }
    }
};

//console.log(merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
console.log(merge([0, 0], 0, [], 0))