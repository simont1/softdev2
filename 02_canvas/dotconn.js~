// Team beaniebaby -- Angela Tom & Simon Tsui
// SoftDev2
// K01 -- I See a Red Door...
// 2019-01-31


var box = true; // 0 for box and 1 for dot

var canvas = document.getElementById("slate");
var ctx = canvas.getContext("2d");

// Clear canvas
var clear = function() {
    ctx.clearRect(0,0,canvas.width,canvas.height);
};

// Toggle between box or dot
var toggle = function() {
    if (box){
        box = false
    } else {
        box = true
    }
    //console.log(box);
};

// Clicking inside canvas
canvas.addEventListener('click', function(e) {
    e.preventDefault(); 
    x = e.offsetX; 
    y = e.offsetY;
    if(box){
        ctx.fillStyle= "#00ff00";
	ctx.fillRect(x,y,100,100);
    } else {
	ctx.fillStyle = "black";
	ctx.beginPath(); // 
	ctx.ellipse(x,y,5,5,0,0,Math.PI*2);
	ctx.fill();
	ctx.stroke();
    }
    
} );

var clear_button = document.getElementById("clear");
clear_button.addEventListener('click', clear);

var toggle_button = document.getElementById("toggle");
toggle_button.addEventListener('click', toggle);

/*
  e.preventDefault() -- Stops the event from occurring
  ctx.beginPath() -- Starts a new path by clearing the past path object 
  e.offsetX -- Retrieves the x coord of the mouse relative to the container that causes the event to occur
  e.offsetY -- Retrieves the y coord of the mouse relative to the container that causes the event to occur

*/
