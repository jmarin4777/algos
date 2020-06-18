// Given an array of citations sorted in ascending order (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

// According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

// Example:

// Input: citations = [0,1,3,5,6]
// Output: 3 
// Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each of them had 
//              received 0, 1, 3, 5, 6 citations respectively. 
//              Since the researcher has 3 papers with at least 3 citations each and the remaining 
//              two with no more than 3 citations each, her h-index is 3.
// Note:

// If there are several possible values for h, the maximum one is taken as the h-index.

var hIndex = function(citations) {
    var h = 0;
    //if the first value is >= the length of the array, the h-index must be equal to the array's length
    if(citations[0]>=citations.length){
        return citations.length
    }
    for(let i=0; i<citations.length; i++){
        //skips any 0 values
        if(citations[i] === 0){
            continue
        }
        var count = 0;
        for(let j=citations.length-1; j>=0; j--){
            //starting at the end of the array, counts papers w/ citations >= to the current paper, i
            if(citations[j] >= citations[i]){
                count++;
            }
            //if the count is > than the current h index, and <= the current paper's number of citations
            //update the h index  
            if(count <= citations[i] && count > h){
                h = count;
                //if the count is exactly equal to the current paper, move on to the next paper
                if(count === citations[i]){
                    break
                }
            }
        }
        //if the number of papers left to check is less than the current h index, the current h index is the maximum value
        if((citations.length - h) <= h){
            return h
        }
        // console.log(count);
    }
    return h
};