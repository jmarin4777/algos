describe("Given an array of citations stored in ascending order,", () => {
    var citations1 = [0,1,3,5,6];
    var citations2 = [100];
    var citations3 = [50, 100];
    var citations4 = [1,1];
    var citations5 = [2,3,4,8,9,9];
    var citations6 = [2,3,5,5,8,9,9];
    
    var hIndex = function(citations) {
        var h = 0;
        if(citations[0]>=citations.length){
            return citations.length
        }
        for(let i=0; i<citations.length; i++){
            if(citations[i] === 0){
                continue
            }
            var count = 0;
            for(let j=citations.length-1; j>=0; j--){
                if(citations[j] >= citations[i]){
                    count++;
                }
                if(count <= citations[i] && count > h){
                    h = count;
                    if(count === citations[i]){
                        break
                    }
                }
            }
            if((citations.length - i - 1) < h){
                return h
            }
            console.log(count);
        }
        return h
    };

    // According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers 
    // have at least h citations each, and the other N − h papers have no more than h citations each."
    it("the h-index should be 1", () => {
        expect(hIndex(citations2)).toEqual(1);
        expect(hIndex(citations4)).toEqual(1);
    });

    it("the h-index should be 2", () => {
        expect(hIndex(citations3)).toEqual(2);
    });
    
    it("the h-index should be 3", () => {
        expect(hIndex(citations1)).toEqual(3);
    });

    it("the h-index should be 4", () => {
        expect(hIndex(citations5)).toEqual(4);
    });

    it("the h-index should be 5", () => {
        expect(hIndex(citations6)).toEqual(5);
    });
});