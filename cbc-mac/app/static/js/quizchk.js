
	$("#Submit").click(function(event){
		console.log("hsiuf");
    	if ($('input[name=Q1]:checked', '#Q-1').val()) {
			A1 = $('input[name=Q1]:checked', '#Q-1').val();
		}
		else
		{
			A1=4;
		}
		if ($('input[name=Q2]:checked', '#Q-2').val()) {
			A2 = $('input[name=Q2]:checked', '#Q-2').val();
		}
		else
		{
			A2=4;
		}
   $.ajax({
        data : {
			Q1:A1,
			Q2:A2
        },
        type : 'POST',
        url : '/check'
      })
      .done(function(data) {
        alert(data.output)
      });
      event.preventDefault();
});

