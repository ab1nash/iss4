
function myArray(arr)
{
	this.sum = function() {
		var s=0;
		for (var i =arr.length - 1; i >= 0; i--) {
		s+=arr[i];
		// console.log(arr[i]);
		}
		return s;
	}


	this.product = function() {
		var p=1;
		for (var i =arr.length - 1; i >= 0; i--) {
		p*=arr[i];
		}

		return p;
	}

	this.modify = function(j) {
		arr[j]+=1;

	}

	this.sort = function() {


	while(1){
			var swapped=0;
			for(var i=0; i<arr.length - 1; i++)
			{if(arr[i]>arr[i+1])
				{var temp=arr[i];
				arr[i]=arr[i+1];
				arr[i+1]=temp;
				swapped=1;}
			}
			if(swapped===0)
				break;
			}
	}

	this.display = function() {
		for (var i = 0; i < arr.length; i++) {
			console.log(arr[i]);

			}

		}	

}

var arr = [1,3,2,4,6,5,7,9,8];

var me = new myArray(arr);
console.log(me.sum());
console.log(me.product());
me.sort();
console.log(me.display());
me.modify(4);
console.log(me.display());

