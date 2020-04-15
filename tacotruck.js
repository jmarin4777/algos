var x = [
    ["x","c","x","x","x","x","x","x","x","x"],
    ["c","x","x","x","x","x","x","x","x","x"],
    ["x","x","x","x","x","x","x","x","x","x"],
    ["x","x","x","x","x","x","x","x","x","x"],
    ["x","x","x","x","x","x","x","x","x","x"],
    ["x","x","x","x","x","x","x","x","x","x"],
    ["x","x","x","x","x","x","x","x","x","x"],
    ["x","x","x","x","x","x","x","x","x","x"],
    ["x","x","x","x","x","x","x","x","c","c"],
    ["x","x","x","x","x","x","x","x","c","c"]
]

var y = [
    [0,1],
    [1,0],  
    [8,8],
    [8,9],
    [9,8],
    [9,9]
]

function original_tacotruck(arr, customers) {
    var xmax = 0
    var xmin = 0
    var ymax = 0
    var ymin = 0
    console.log(arr)
    for(var i=0;i<customers.length;i++){
        for(var j=0;j<customers[i].length;j++){
            if(j==0 && customers[i][j]<xmin){
                xmin = customers[i][j]
            }
            if(j==0 && customers[i][j]>xmax){
                xmax = customers[i][j]
            }
            if(j==1 && customers[i][j]<ymin){
                ymin = customers[i][j]
            }
            if(j==1 && customers[i][j]>ymax){
                ymax = customers[i][j]
            }
        }   
    }
    var x = (xmax - xmin)/2
    var y = (ymax - ymin)/2
    console.log(x, y)
    arr[x][y] = "t"
    console.log(arr)
    return arr
}
// original_tacotruck(x,y)

function new_tacotruck(arr, customers){
    var xsum = 0
    var ysum = 0 
    console.log(arr)
    for(var i=0;i<customers.length;i++){
        for(var j=0;j<customers[i].length;j++){
            if(j==0){
                xsum += customers[i][j]
            }
            if(j==1){
                ysum += customers[i][j]
            }
        }   
    }
    var xavg = Math.round(xsum/customers.length)
    var yavg = Math.round(ysum/customers.length)
    console.log(xavg, yavg)
    arr[xavg][yavg] = "t"
    console.log(arr)
    return arr
}
new_tacotruck(x,y)