// String: Rotate String
// Create a standalone function that accepts a string and an integer, and rotates the string to the right by that amount. (Ex: Given "Boris Godunov", 5 => "dunovBoris Go")
function rotateString(str,num){
    var arr = str.split("");
    // console.log("beginning array: ", arr);
    for (var i = str.length-1; i > str.length-1-num; i--){
        arr.unshift(arr.pop());
        // console.log(arr)
    }
    var newStr = arr.join("")
    return newStr;
}
console.log(rotateString("Boris Godunov", 5))

// String: Is Rotation
// Create the function isRotation(str1,str2), that returns whether the second string is a rotation of the first. Would you change your implementation if you knew that the two were usually entirely unrelated?

function isRotation1(str1, str2){
    if (str1.length != str2.length){
        return false;
    }
    for(var i = 0; i < str1.length; i++){
        var count = 0;
        var j = i;
        var checker = "";
        while(count < str1.length){
            if(j == str1.length){
                j = 0;
            }
            checker += str2[j];
            j++;
            count++;
        }
        if(checker == str1){
            return true
        }
    }
    return false
}
console.log(isRotation1("Boris Godunov","dunovBoris Go"))

function isRotation2(str1, str2){
    if (str1.length != str2.length){
        return false;
    }
    tempStr = str1 + str1;
    if (tempStr.includes(str2)){
        return true;
    }
    else {
        return false;
    }
}
console.log(isRotation2("Boris Godunov","dunovBoris Go"))