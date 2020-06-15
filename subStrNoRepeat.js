// Given a string, find the length of the longest substring without repeating characters.

// Example 1:

// Input: "abcabcbb"
// Output: 3 
// Explanation: The answer is "abc", with the length of 3. 
// Example 2:

// Input: "bbbbb"
// Output: 1
// Explanation: The answer is "b", with the length of 1.
// Example 3:

// Input: "pwwkew"
// Output: 3
// Explanation: The answer is "wke", with the length of 3. 
//              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

var lengthOfLongestSubstring = function(s) {
    if(s.length === 0){
        return 0
    }
    var dict = {};
    var arr = [];
    for(let i=0; i<s.length; i++){
        arr.push("");
        for(let j=i; j<s.length; j++){
            if(dict[s[j]]){
                dict = {};
                break
            } else{
                dict[s[j]] = s[j];
                arr[arr.length-1] += s[j];
            }
        }
        if(i>0){
            if(arr[1].length > arr[0].length){
                arr.shift()
            } else{
                arr.pop()
            }
        }
    }
    console.log(arr);
    return arr[0].length
};

lengthOfLongestSubstring("dvdf"); // "vdf" -> 3