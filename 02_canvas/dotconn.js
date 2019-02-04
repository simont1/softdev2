// Team beaniebaby -- Angela Tom & Simon Tsui
// SoftDev2
// K02 -- Connecting the Dots
// 2019-02-04

var first = true;

var canvas = document.getElementById("playground");
var ctx = canvas.getContext("2d");

// Clear canvas
var clear = function() {
    ctx.clearRect(0,0,canvas.width,canvas.height);
    first = true;
};


// Clicking inside canvas
canvas.addEventListener('click', function(e) {
    x = e.offsetX; 
    y = e.offsetY;
    ctx.fillStyle = "black";
    if (first){
	ctx.beginPath(); //
	ctx.fillStyle = "red";
	ctx.ellipse(x,y,5,5,0,0,Math.PI*2);
	ctx.fill();
	ctx.stroke();
	first = false;
    }else{
	ctx.lineTo(x,y);
	ctx.moveTo(x,y);
	ctx.fillStyle= "red";
	ctx.ellipse(x,y,5,5,0,0,Math.PI*2);
	ctx.fill();
	ctx.stroke();
	ctx.moveTo(x,y);
    }
});	
		       

var clear_button = document.getElementById("clear");
clear_button.addEventListener('click', clear);

