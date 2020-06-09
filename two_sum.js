// Given an array of integers, return indices of the two numbers such that they add up to a specific target.

// You may assume that each input would have exactly one solution, and you may not use the same element twice.

// Example:
// Given nums = [2, 7, 11, 15], target = 9,
// Because nums[0] + nums[1] = 2 + 7 = 9,
// return [0, 1].
nums = [2, 7, 11, 15];
target = 9;
var twoSum = function(nums, target) {
    var sum = 0;
    for(var i=0;i<nums.length-1;i++){
        for(var j=i+1;j<nums.length;j++){
            sum = nums[i] + nums[j];
            if(sum == target){
                return [i, j]
            }   
        }
    }
};
console.log(twoSum(nums, target));