//Simon Tsui
//Softdev pd07
//K09 -- basic SVG work
//2019-03-13w


var pic = document.getElementById("vimage");
var button = document.getElementById("but_clear");

var lastx = -1;
var lasty = -1;

pic.addEventListener('click', function(e){
  var c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
  c.setAttribute("cx", e.offsetX);
  c.setAttribute("cy", e.offsetY);
  c.setAttribute("r", 10);
  c.setAttribute("fill", "red");
  c.setAttribute("stroke", "black");
  pic.appendChild(c);

  if (lastx != -1){
    var l = document.createElementNS("http://www.w3.org/2000/svg", "line");
    l.setAttribute("x1", lastx);
    l.setAttribute("y1", lasty);
    l.setAttribute("x2", e.offsetX);
    l.setAttribute("y2", e.offsetY);
    l.setAttribute("stroke", "black");
    pic.appendChild(l);
  }
  lastx = e.offsetX;
  lasty = e.offsetY;
});

button.addEventListener('click', function(e){
  while (pic.lastChild) {
    pic.removeChild(pic.lastChild);
    lastx = -1;
    lasty = -1;
}
});
