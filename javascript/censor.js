var str = "snap crackle pop nincomPooP!";
var arr = ["crack", "poop"]
// function censor(str){
//     str = str.replace(/crack/gi, "*****");
//     str = str.replace(/poop/gi, "****");
//     console.log(str)
//     return str
// }
// censor(str);

function censor2(str, word){
    var strArr = str.split(" ");
    for(var i=0; i<strArr.length; i++){
        var count = 0;
        var k = 0;
        var newstr = "";
        for(var j=0; j<strArr[i].length; j++){
            if(strArr[i][j].toUpperCase() == word[k] || strArr[i][j].toLowerCase() == word[k]){
                if(count == 0){
                    var start = j;
                }
                k++;
                count++;
                newstr += "*"
                if(count == word.length){
                    strArr[i] = newstr + strArr[i].slice(start+count);
                }
            } else{
                newstr += strArr[i][j];
            }
        }
    }
    return strArr.join(" ")
}
for(var word of arr){
    str = censor2(str, word);
    console.log(str);
}