// There are two sorted arrays nums1 and nums2 of size m and n respectively.

// Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

// You may assume nums1 and nums2 cannot be both empty.

// Example 1:

// nums1 = [1, 3]
// nums2 = [2]

// The median is 2.0
// Example 2:

// nums1 = [1, 2]
// nums2 = [3, 4]

// The median is (2 + 3)/2 = 2.5

var findMedianSortedArrays = function(nums1, nums2) {
    var length = nums1.length + nums2.length;
    var parity;
    if(length%2 === 0){
        length = length/2;
        parity = 2;
    } else{
        length = Math.floor(length/2);
        parity = 1;
    }
    var count = 0, i = 0, j = 0;
    var temp = [];
    while(count <= length){
        if(i === nums1.length){
            temp.push(nums2[j]);
            j++;
        } else if(j === nums2.length){
            temp.push(nums1[i]);
            i++;
        } else{
            if(nums1[i] > nums2[j]){
                temp.push(nums2[j]);
                j++;
            } else if(nums1[i] < nums2[j]){
                temp.push(nums1[i]);
                i++;
            } else {
                temp.push(nums1[i]);
                i++;
            }
        }
        if(temp.length>parity){
            temp.shift();
        }
        count++;
    }
    if(parity === 2){
        return (temp[0]+temp[1])/2
    } else{
        return temp[0]
    }
};