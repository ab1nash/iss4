function getMeNextFirst(s){
	s=s.trim();
	var t=s.split(' ');
	for(i=0;i<t.length-1;i++)
	{
		t[i]+=t[i+1].substr(0,1);
		t[i+1]=t[i+1].substr(1);

	}
	return t.join(' ');
}
console.log(getMeNextFirst("hello World !!"));