const questionsArr = ["Are You a Gay?","a","b"]
const wantedQuestion = "Are You a Gay?"
let currentQuestion = 0

function onYes(){
    if(currentQuestion >= questionsArr.length){
        currentQuestion = 0
    }

    document.getElementById("question").innerHTML = questionsArr[currentQuestion]
    currentQuestion++
}

function onNo(){
    if(wantedQuestion != document.getElementById("question").innerHTML){
        document.getElementById("question").innerHTML = questionsArr[currentQuestion]
        currentQuestion++
    }  
}

function teleport(){
    if(wantedQuestion != document.getElementById("question").innerHTML){
        return;
    }
    
    var button = document.getElementById("No_button")

    var maxTop = window.innerHeight-button.clientHeight;
    var maxLeft = window.innerWidth - button.clientWidth;

    var randomTop = Math.floor(Math.random() * maxTop);
    var randomLeft = Math.floor(Math.random() * maxLeft);

    button.style.top = randomTop + "px";
    button.style.left = randomLeft +"px";
}

