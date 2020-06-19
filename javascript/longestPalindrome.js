// Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

// Example 1:

// Input: "babad"
// Output: "bab"
// Note: "aba" is also a valid answer.
// Example 2:

// Input: "cbbd"
// Output: "bb"

const longestPalindrome = (s) => {
    if(s.length <= 1){
        return s
    }
    var longest = s.substring(0, 1);
    for(let i=0; i<s.length; i++){
        let temp = expand(s, i, i);
        let temp1 = expand(s, i, i+1);
        if(temp1.length > temp.length){
            temp = temp1;
        }
        if(temp.length > longest.length){
            longest = temp;
        }
    }
    return longest
}

const expand = (s, start, end) => {
    while(start >= 0 && end < s.length && s[start] === s[end]){
        start--;
        end++;
    }
    return s.substring(start + 1, end)
}

console.log(longestPalindrome("cbbd"));