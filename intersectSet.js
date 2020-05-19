function intersect (arr1, arr2) {
    var newarr = [];
    let dict = {};
    for(i = 0; i < arr1.length; i ++){
        if(dict[arr1[i]]){
            dict[arr1[i]] += 1;
        } else{
            dict[arr1[i]] = 1;
        }
    }
    for(j = 0; j < arr2.length; j++){
        if(dict[arr2[j]] > 0){
            dict[arr2[j]] -= 1;
            newarr.push(arr2[j]);
        }
    }
    console.log(newarr);
    return newarr
}
intersect([1,2,2,7], [2,2,2,6,6,7])