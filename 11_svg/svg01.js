// Simon Tsui
// Softdev2 pd07
// K11 -- Ask Circles [Change || Die] …While On The Go
// 2019-03-18m

var pic = document.getElementById("vimage");
var mv = document.getElementById("move");
var scr = document.getElementById("scramble");
var clr = document.getElementById("clear");
var id = 0;

var circles = [];

var clicked = false;

var addCircle = function(x, y){
  var c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
  c.setAttribute("cx", x);
  c.setAttribute("cy", y);
  c.setAttribute("r", 15);
  c.setAttribute("fill", "blue");
  c.setAttribute("stroke", "black");
  pic.appendChild(c);
  c.x = x;
  c.y = y;
  c.xVel = 1;
  c.yVel = 1;
  circles.push(c);
  return c;
}

var setCircle = function(c){
  c.addEventListener('click', function(){
    if (c.getAttribute("fill") == "blue")
      c.setAttribute("fill", "green");
    else {
      c.remove();
      var newC = addCircle(Math.random() * pic.getAttribute("width"),
                        Math.random() * pic.getAttribute("height"));
      pic.appendChild(newC);
      setCircle(newC);
    }
    clicked = true;
  });
}

pic.addEventListener('click', function(e){
  if (!clicked){
    var c = addCircle(e.offsetX, e.offsetY);
    setCircle(c);
  }
  clicked = false;
});

clr.addEventListener('click', function(e){
  while (pic.firstChild)
    pic.removeChild(pic.firstChild);
});

var moveCircle = function(){
  id = window.requestAnimationFrame(moveCircle);
  var c, r;
  for (i = 0; i < circles.length; i ++){
    c = circles[i];
    r = c.getAttribute("r");
    c.x += c.xVel;
    c.y += c.yVel;
    c.setAttribute("cx", c.x);
    c.setAttribute("cy", c.y);
    if (c.x >= pic.getAttribute("width") - r)
      c.xVel = -Math.abs(c.xVel);
    if (c.x <= r)
      c.xVel = Math.abs(c.xVel);
    if (c.y >= pic.getAttribute("height") - r)
      c.yVel = -Math.abs(c.yVel);
    if (c.y <= r)
      c.yVel = Math.abs(c.yVel);
  }
}

mv.addEventListener('click', function(){
  window.cancelAnimationFrame(id);
  moveCircle();
});

scr.addEventListener('click', function(){
  var newx, newy;
  for (i = 0; i < circles.length; i ++){
    newx = Math.random() * 500;
    newy = Math.random() * 500;
    circles[i].x = newx;
    circles[i].y = newy;
  }
})
