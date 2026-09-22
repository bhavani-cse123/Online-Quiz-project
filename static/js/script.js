let time =60;
const timer=setInterval(function(){
    time--;
    document.getElementById("time").textContent=time;
    if(time<=0){
        clearInterval(timer);
        alert("time is up");
        document.getElementById("quizform").submit();
    }
},1000);
