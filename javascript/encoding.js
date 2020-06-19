function encode(str){
    var newstr = "";
    for(var i=0; i<str.length; i++){
        if(str[i+1] != str[i]){
            var count = 0;
            var j = i;
            while(str[j] == str[i]){
                count++;
                j--;
            }
            newstr += str[i]+count;
        }
    }
    return console.log(newstr);
}
encode("abbcccddddeeeeeffffffaaa") // -> a1b2c3d4e5f6a3

function decode(str){
    var nums = [];
    var newstr = "";
    for(var i=0; i<str.length; i++){
        var num_to_add = "";
        var j=i;
        while(str[j] < ":" && str[j] > "/"){
            num_to_add += str[j];
            j++;
            i++;
        }
        if(num_to_add != ""){
            nums.push(Number(num_to_add));
        }
    }
    var count = 0;
    for(var i=0; i<str.length; i++){
        if(str[i] >= "A"){
            newstr += str[i].repeat(nums[count]);
            count++
        }
    }
    console.log(newstr);
}
decode("a10b2c3d4e5f6a3") // => "aaaaaaaaaabbcccddddeeeeeffffffaaa"