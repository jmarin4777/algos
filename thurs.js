// Loop over the larger array to find the vlues of the smaller array to check the values
x = [
    [1,25,35,97,74,4,5,1,2,3],
    [1,25,36,98,74,4,5,1,2,3],
    [1,25,36,98,74,4,5,1,2,3],
    [1,25,36,98,74,4,5,1,2,3],
    [1,25,36,98,74,4,5,1,2,3]

]

y = [
    [25,36,98], //arr[j], arr[j+1], arr[j+2]
    [36,98],
    [36,98]
]

function abc(arr,val){
    for(var x = 0; x < val.length; x++){
        for(var y = 0; y<x.length; y++){
        }
    }
    var runner = 0
    var checker = 0
    while (runner < val.length) {
        for(var i = 0; i < arr.length; i++){
            for(var j = 0; j<i.length; j++){
                if(arr[i][j] == val[runner][checker]){
                    for(var k=0; k<val[runner].length; k++){
                        if(arr[i][j+k] == val[runner][k]){
                            
                        }
                    }
                }
            }
        }
        runner++
    }
}

// var fruits = ["Banana", "Orange", "Apple", "Mango"];
// var n = fruits.includes("Mango");

// var fruits = ["Banana", "Orange", "Apple", "Mango"];
// var a = fruits.indexOf("Apple");

