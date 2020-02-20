/**
 * Created by Ramakrishna on 21-11-2019.
 */

$(document).ready(function() {
        window.history.pushState(null, "", window.location.href);
        window.onpopstate = function() {
            window.history.pushState(null, "", window.location.href);
        };
});

//Full Name validation -----------------
function allLetter(uname)
{
var letters = /^[A-Za-z ]+$/;
if(uname.value.match(letters))
{
return true;
}
else
{
alert('Full name must have alphabet characters only');
uname.focus();
return false;
}
}

//Signum Validation ---------
function signumValidation(signum)
{
if(signum.value.toLowerCase().startsWith("e") && signum.value.length==7)
{
return true;
}
else
{
alert('Input valid Signum');
signum.focus();
return false;
}
}

function validateEmail(email) {
  var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  return re.test(email);
}

var manageradiorel = "";

//Login Form submit click---------------
 $("#login_form").submit(function(e){
       e.preventDefault();
       manageradiorel = $("input:radio[name ='gender']:checked").val();

       if(allLetter(document.forms["login_form"]["fullname"])){
       if(signumValidation(document.forms["login_form"]["signumname"])){

        $.post("/quiz/dashboard/",
           {
               fullname : document.forms["login_form"]["fullname"].value,
               signumname : document.forms["login_form"]["signumname"].value,
               email : document.forms["login_form"]["email"].value,
               gender : manageradiorel,
               exp : document.forms["login_form"]["exp"].value,
               csrfmiddlewaretoken : document.forms["login_form"]["csrfmiddlewaretoken"].value
           },
           function(data,status)
           {
               window.location.href="/quiz/dashboard/";
           }
       );
       }
       }
 });

var val1="";
var val2="";
var val3="";
var val4="";

 $("#dash_form").submit(function(e){
      e.preventDefault();
        if (document.forms["dash_form"]["abcId"].value == "6/") {
         $.post("/quiz/chart/",
           {
               choice1 : val1,
               choice2 : val2,
               choice3 : val3,
               csrfmiddlewaretoken : document.forms["dash_form"]["csrfmiddlewaretoken"].value
           },
           function(data,status)
           {
               window.location.href="/quiz/chart/";
           }
       );
        }else{
        if(document.getElementById("div21").childNodes.length == 0){
            document.getElementById("div21").style["border"] = "2px solid red";
       }else if(document.getElementById("div22").childNodes.length == 0){
            document.getElementById("div22").style["border"] = "2px solid red";
       }else if(document.getElementById("div23").childNodes.length == 0){
            document.getElementById("div23").style["border"] = "2px solid red";
       }else{

        $.post("/quiz/question/",
           {
               choice1 : val1,
               choice2 : val2,
               choice3 : val3,
               image : document.getElementById("image_data").value,
               csrfmiddlewaretoken : document.forms["dash_form"]["csrfmiddlewaretoken"].value
           },
           function(data,status)
           {
                 $("#progress-bar").css("width", "48%");
                $("#progress-bar").attr("aria-valuenow", "48%");
               window.location.href="/quiz/question/";
           }
       );
       }
       }
 });

 function allowDrop(ev) {
  ev.preventDefault();
}

function drag(ev) {
  ev.dataTransfer.setData("text", ev.target.id);
}

function drop1(ev) {
  ev.preventDefault();
  var data = ev.dataTransfer.getData("text");
  if(document.getElementById("div21").childNodes.length == 0){
     document.getElementById("div21").style["border"] = "2px solid white";
    val1 = document.getElementById(data).alt;
  ev.target.appendChild(document.getElementById(data));

  }
}

function drop2(ev) {
  ev.preventDefault();
  var data = ev.dataTransfer.getData("text");
  if(document.getElementById("div22").childNodes.length == 0){
   document.getElementById("div22").style["border"] = "2px solid white";
  val2 = document.getElementById(data).alt;
  ev.target.appendChild(document.getElementById(data));
 }
}

function drop3(ev) {
  ev.preventDefault();
  var data = ev.dataTransfer.getData("text");
  if(document.getElementById("div23").childNodes.length == 0){
   document.getElementById("div23").style["border"] = "2px solid white";
  val3 = document.getElementById(data).alt;
  ev.target.appendChild(document.getElementById(data));
  }
}

function drop11(ev) {
  ev.preventDefault();
  var data = ev.dataTransfer.getData("text");
  if(document.getElementById(data).id.toString()=="drag11"){
     ev.target.appendChild(document.getElementById(data));
  }
}

function drop12(ev) {
  ev.preventDefault();
  var data = ev.dataTransfer.getData("text");
  if(document.getElementById(data).id.toString()=="drag12"){
     ev.target.appendChild(document.getElementById(data));
  }
}

function drop13(ev) {
  ev.preventDefault();
  var data = ev.dataTransfer.getData("text");
  if(document.getElementById(data).id.toString()=="drag13"){
     ev.target.appendChild(document.getElementById(data));
  }
}

function drop14(ev) {
  ev.preventDefault();
  var data = ev.dataTransfer.getData("text");
  if(document.getElementById(data).id.toString()=="drag14"){
     ev.target.appendChild(document.getElementById(data));
  }
}

function drop15(ev) {
  ev.preventDefault();
  var data = ev.dataTransfer.getData("text");
  if(document.getElementById(data).id.toString()=="drag15"){
     ev.target.appendChild(document.getElementById(data));
  }
}

function drop16(ev) {
  ev.preventDefault();
  var data = ev.dataTransfer.getData("text");
  if(document.getElementById(data).id.toString()=="drag16"){
     ev.target.appendChild(document.getElementById(data));
  }
}


 function validation(data1, data2, data3){
    if(data1==0){
        return false;
    }else if(data2==0){
     return false;
    }else if(data3==0){
     return false;
    }else{
     return true;
    }
}
