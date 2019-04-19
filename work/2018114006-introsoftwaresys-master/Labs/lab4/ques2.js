function altSpaceToUnderscore(s)
{
	s=s.trim();

	var word = s.split(' ');
	var space = s.split(' ').length-1;
	var l='';

	for(var i=0;i<space;i++){
		l+=word[i];
		if(i%2==1)
			l+='_';
		else
			l+=' ';
	} 

	l+=word[word.length-1];

	return l;

}

// o = altSpaceToUnderscore("   jashn arora is a good boy  ");
// console.log(o);



