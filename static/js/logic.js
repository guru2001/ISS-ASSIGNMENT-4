document.getElementById("matrix1").style.display = "none";	
document.getElementById("matrix2").style.display = "none";
document.getElementById("f1").style.display="none";
document.getElementById("f2").style.display="none";
document.getElementById("f3").style.display="none";
document.getElementById("f4").style.display="none";
document.getElementById("b").style.display="none";
document.getElementById("b1").style.display="none";
document.getElementById("b2").style.display="none";
function Answer()
{
	if(a==0)
	{
	document.getElementById("matrix1").style.display="block";
	document.getElementById("matrix2").style.display="block";
		a=1;
	}
	else 
	{
		document.getElementById("matrix1").style.display="none";
	document.getElementById("matrix2").style.display="none";
		a=0;
	}
}
function Answer2()
{
	if(b==0)
	{
	b=1;
	document.getElementById("matrix1").style.display="block";
	}
	else 
	{
	b=0;
	document.getElementById("matrix1").style.display="none";
	}
}
function Answer3()
{
	if(c==0)
	{
	c=1;
	document.getElementById("matrix2").style.display="block";
	}
	if(c==1)
	{
		c=0;
		document.getElementById("matrix2").style.display="none";

	}
}
