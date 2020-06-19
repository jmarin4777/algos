function str_to_word(str){
    var arr = [];
    var j = 0;
    var punc = ["?", "!", ".", ","]
    for(var i=0; i<str.length; i++){
        if(str[i] == " " || str[i] == "\n" || str[i] == "\t"){
            if(arr[j] != undefined){
                j++;
            }
        } else if(punc.includes(str[i])){
            j++;
            arr[j] = str[i];
            j++;
        } else{
            if(arr[j]){
                arr[j] += str[i];
            } else{
                arr[j] = str[i];
            }
        }
    }
    console.log(arr);
    return arr
}
str_to_word('My Name is Bob!')

function reverse_word(str){
    var arr = str_to_word(str);
    var str = "";
    for(var i=arr.length-1; i>=0; i--){
        if(i == 0){
            str += arr[i];
        } else{
            str += arr[i];
            str += " ";
        }
    }
    console.log(str);
    return str
}
reverse_word("This is a test")
reverse_word("Life is not a drill, go for it!")