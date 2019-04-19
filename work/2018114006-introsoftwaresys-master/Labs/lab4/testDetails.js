var value = require('./ISS-lab4/data.js')

function getHighestMarks(){
    var maximum=0;
    var l;
    
    for( var name in value ){
        var sum=0;
        for(var i=0;i<5;i++)
            sum+=value[name][i];
        if(sum>maximum){
            maximum=sum;
            l=name;
        }
    }
    return l;
}

function getSubject2Toppers(){
    var arr=[]
    for(name in value){
         arr.push([name,value[name][1]])
    }
    arr.sort(function(a,b){return a[1] - b[1]});
    arr.reverse();
    var ret=[]
    
    for(var element in arr)
        ret.push(arr[element][0])
    return ret
}

