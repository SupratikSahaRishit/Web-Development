var dices = ['1', '2', '3', '4', '5', '6'];
var stopped = true;


function change() {
    var random = Math.floor(Math.random() * 6);
    dice.innerHTML = dices[random];
}

function stopStart() {
    if (stopped) {
        stopped = false;
       
        t = setInterval(change, 100);
    } else {
        clearInterval(t);
        stopped = true;
    }
}


window.onload = function() {
    dice = document.getElementById("dice");
    stopStart();
}
