$(document).ready(function() 
{

	$("#form").click(function(event){
	
		$.ajax({
			data : {
				e0 : $('#e0').val(),			//Post a ajax request for pushing to flask
				e1 : $('#e1').val(),
				e2 : $('#e2').val(),			
				e3 : $('#e3').val(),
				e4 : $('#e4').val(),
				e5 : $('#e5').val(),
				e6 : $('#e6').val(),
				e7 : $('#e7').val(),
				e8 : $('#e8').val(),
				e9 : $('#e9').val(),
				e10 : $('#e10').val(),
				e11 : $('#e11').val(),
				e12 : $('#e12').val(),
				e13 : $('#e13').val(),
				e14 : $('#e14').val(),
				e15 : $('#e15').val(),
				e16 : $('#e16').val(),
				e17 : $('#e17').val(),
				e18 : $('#e18').val(),
				e19 : $('#e19').val(),
				e20 : $('#e20').val(),
				e21 : $('#e21').val(),
				e22 : $('#e22').val(),
				e23 : $('#e23').val(),
				e24 : $('#e24').val(),
				e25 : $('#e25').val(),
				e26 : $('#e26').val(),
				e27 : $('#e27').val(),
				t0 : $('#t0').val(),
				t1 : $('#t1').val(),
				t2 : $('#t2').val(),
				t3 : $('#t3').val(),
				t4 : $('#t4').val(),
				t5 : $('#t5').val(),
				t6 : $('#t6').val(),
				t7 : $('#t7').val(),
				t8 : $('#t8').val(),
				t9 : $('#t9').val(),
				t10 : $('#t10').val(),
				t11 : $('#t11').val(),
				t12 : $('#t12').val(),
				t13 : $('#t13').val(),
				t14 : $('#t14').val(),
				t15 : $('#t15').val(),
				t16 : $('#t16').val(),
				t17 : $('#t17').val(),
				t18 : $('#t18').val(),
				t19 : $('#t19').val(),
				t20 : $('#t20').val(),
				t21 : $('#t21').val(),
				t22 : $('#t22').val(),
				t23 : $('#t23').val(),
				t24 : $('#t24').val()
			},                       
			type : 'POST',                //POST to process URL
			url : '/process'
		})
		.done(function(data) 
		{
			console.log(data);
			if(data.error)				//If error is returned,give a alert box
			{
				
			window.alert("Please fill all boxes");
			}
			else
			{
			document.getElementById("matrix1").style.display="none";   //Hide everything once the button is hit
			document.getElementById("matrix2").style.display="none";
			document.getElementById("f1").style.display="none";
			document.getElementById("f2").style.display="none";
			document.getElementById("f3").style.display="none";
			document.getElementById("f4").style.display="none";
			document.getElementById("b").style.display="none";
			document.getElementById("b1").style.display="none";
			document.getElementById("b2").style.display="none";
				
			for(var i=0;i<28;i++)
			{
				var str1="e";
				var res = str1 + i;
				// console.log(res);
				document.getElementById(res).style.backgroundColor = "white";

			}	
				for(var i=0;i<25;i++)
			{
				var str1="t";
				var res = str1 + i;
				document.getElementById(res).style.backgroundColor = "white";
			}
			if(data[0]==-2)                                            //Logic part if only transition is wrong print transition matrix only and similarly for
																	//emmisssion matrix and both are wrong print both when button is pressed
			{
			document.getElementById("f1").style.display="block";	
			}
			else if(data[0]==-1)
			{
			document.getElementById("f4").style.display="block"	
			document.getElementById("b2").style.display="block";
			}
			else if(data[0]==0)
			{
			document.getElementById("f3").style.display="block";	
			document.getElementById("b1").style.display="block";
			}
			else if(data[0]==1)
			{
			document.getElementById("f2").style.display="block";	
			document.getElementById("b").style.display="block";
			}
			console.log(data);

			for(var i=1;i<data.length;i++)
			{
				document.getElementById(data[i]).style.backgroundColor = "red";
			}

			}
	
			});
		event.preventDefault();
	});

});