// azrael --- Jason Tung and Simon Tsui
// SoftDev2 pd7
//K #03: They lock us in the tower whenever we get caught
// 2019-02-04

//getting references to html elements
var c = document.getElementById("playground");
var ctx = c.getContext("2d");
var stop = document.getElementById("stop");
var circle = document.getElementById("circle");
var dvd = document.getElementById("dvd");

//initializing requisite variables
var requestID;
var currentlyDoing = "none";

//circle properties
var radius;
var growing;

//dvd properties
var randXStart;
var randYStart;
var dvdVeloc;
var dvdXY;

//set the fill colors now
ctx.fillStyle = "red";
ctx.strokeStyle = "black";

var drawCircle = function (x, y, r) {
    ctx.beginPath();
    ctx.ellipse(x, y, r, r, 0, 0, 2 * Math.PI);
    ctx.stroke();
    ctx.fill();
};

//drawCircle(c.width / 2, c.height / 2, radius);

var clear = function () {
    ctx.clearRect(0, 0, c.width, c.height);
};

var drawDot = function () {
    window.cancelAnimationFrame(requestID);
    clear();
    if (Math.abs(radius - 45) >= 45) {
        growing = radius == 90 ? -1 : 1;
    }
    //console.log(growing);
    radius += growing;
    drawCircle(c.width / 2, c.height / 2, radius);
    requestID = window.requestAnimationFrame(drawDot);
};

var runDot = function () {
    if (currentlyDoing !== "circle") {
        radius = 0;
        growing = 1;
        currentlyDoing = "circle";
    }
    drawDot();
};

var bounce = function () {
    for (var i = 0; i < 2; i++) {
        var buffer = i === 0 ? 40 : 25;
        if (Math.abs(250 - (dvdXY[i] + 50)) >= c.width / 2 - buffer) {
            dvdVeloc[i] *= -1;
        }
    }
};

var drawDvd = function () {
    window.cancelAnimationFrame(requestID);
    clear();
    var logo = new Image();
    logo.src = "logo_dvd.jpg";
    ctx.drawImage(logo, dvdXY[0], dvdXY[1], 100, 100);
    //drawCircle(dvdXY[0], dvdXY[1], 10);
    dvdXY[0] += dvdVeloc[0];
    dvdXY[1] += dvdVeloc[1];
    bounce();
    requestID = window.requestAnimationFrame(drawDvd);
};

//diagnostic to make sure it's all good
var coltbl = {"q1": 0, "q2": 0, "q3": 0, "q4": 0};
var magnitudetbl = {"x": 0, "y": 0};

var runDvd = function () {
    if (currentlyDoing !== "dvd") {
        var theta = Math.random() * Math.PI * 2;
        var randXStart = 4 * Math.sin(theta);
        var randYStart = 4 * Math.cos(theta);
        dvdVeloc = [Math.random() < .5 ? randXStart : -randXStart, Math.random() < .5 ? randYStart : -randYStart];
        console.log(dvdVeloc);
        console.log("this is y");
        console.log(randYStart);
        dvdVeloc = [Math.random() < .5 ? randXStart : -1 * randXStart, Math.random() < .5 ? randYStart : -1 * randYStart];
        console.log(dvdVeloc);
        if (Math.abs(dvdVeloc[0]) > Math.abs(dvdVeloc[1])) {
            magnitudetbl.x++;
        }
        else {
            magnitudetbl.y++;
        }
        console.log("magnitudes:");
        console.log(magnitudetbl);
        dvdXY = [Math.random() * (c.width - 80), Math.random() * (c.height - 80)];
        currentlyDoing = "dvd";
    }

    drawDvd();
};

var stopIt = function () {
    window.cancelAnimationFrame(requestID);
};

circle.addEventListener("click", runDot);
stop.addEventListener("click", stopIt);
dvd.addEventListener("click", runDvd);

