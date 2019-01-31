var canvas = document.getElementById("slate");
var ctx = canvas.getContext("2d");
var rect = true;
ctx.fillStyle = "#0000BB";


var clear = document.getElementById("clear");
//helper clear
var clear2 = function(){
  ctx.clearRect(0, 0, 600, 600);
  console.log("Canvas Cleared!");
}
clear.addEventListener("click", clear2);


var toggle = document.getElementById("toggle");

toggle.addEventListener('click', function(){
  rect = !rect;
  console.log("Shape has been switched!")
})

var clickerHelper = function(e){
  var r = canvas.getBoundingClientRect();
  console.log(r);
  var x = e.clientX - r.left;
  var y = e.clientY - r.top;
  if (rect){
    ctx.fillRect(x - 25, y - 25, 50, 50);
  }
  else {
    ctx.beginPath();
    ctx.arc(x, y, 5, 0, 2 * Math.PI, true);
    ctx.fill();
    ctx.stroke();
  }
}
canvas.addEventListener('click', clickerHelper);
