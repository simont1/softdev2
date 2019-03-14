//Simon Tsui
//Softdev pd07
//K10 -- Ask Circles [Change || Die]
//2019-03-14r


var pic = document.getElementById("vimage");
var button = document.getElementById("but_clear");
var clicked = false;

var addCircle = function(x, y){
  var c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
  c.setAttribute("cx", x);
  c.setAttribute("cy", y);
  c.setAttribute("r", 15);
  c.setAttribute("fill", "blue");
  c.setAttribute("stroke", "black");
  pic.appendChild(c);
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

pic.addEventListener("click", function(e){
  if(!clicked){
    var c = addCircle(e.offsetX, e.offsetY);
    setCircle(c);
  }
  clicked = false;
});

button.addEventListener('click', function(e){
  while (pic.lastChild) {
    pic.removeChild(pic.lastChild);
}
});
