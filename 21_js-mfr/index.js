/*
Simon Tsui
Softdev pd7
K21 -- Onions, Bell Peppers, and Celery, Oh My!
2019-04-30t
*/

function readJSON(file) {
  var request = new XMLHttpRequest();
  request.open('GET', file, false);
  request.send(null);
  if (request.status == 200)
  return request.responseText;
};
var temp = JSON.parse(readJSON('testData.json'));

var G6 = function(e){
  var num = temp.reduce(function(a,b){
    if(b.grade6 != null && b.schoolyear == 20052006){
      return a + b.grade6
    }
    return a
  }, 0)
  return num
}

var numHisp = function(e){
  var num = temp.filter(function(n){
    return (n.hispanic_per > 50)
  })
  return num.length / temp.length * 100
}



var K12 = function(e){
  var num = temp.filter(function(n){
    return (n.grade1 != null && n.grade12 != null)
  })
  return num.length
}


var sixthGrade = document.getElementById("G6")
sixthGrade.innerHTML = G6()
var perHisp = document.getElementById("hisp")
perHisp.innerHTML = numHisp()
var allGrades = document.getElementById("K12")
allGrades.innerHTML = K12()

console.log(temp[0])
console.log(G6)
