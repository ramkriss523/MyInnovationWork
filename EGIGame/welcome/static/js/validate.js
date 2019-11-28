/**
 * Created by Ramakrishna on 21-11-2019.
 */
 $("#login_form").submit(function(e){
       e.preventDefault();

        $.post("/quiz/dashboard/",
           {
               fullname : document.forms["login_form"]["fullname"].value,
               signumname : document.forms["login_form"]["signumname"].value,
               csrfmiddlewaretoken : document.forms["login_form"]["csrfmiddlewaretoken"].value
           },
           function(data,status)
           {
               window.location.href="/quiz/dashboard/";
           }
       );
 });


 $("#dash_form").submit(function(e){
      e.preventDefault();

        if (document.forms["dash_form"]["abcId"].value == "6/") {
         $.post("/quiz/chart/",
           {
               csrfmiddlewaretoken : document.forms["dash_form"]["csrfmiddlewaretoken"].value
           },
           function(data,status)
           {
               window.location.href="/quiz/chart/";
           }
       );
        }else{
        $.post("/quiz/question/",
           {
               choice1 : document.forms["dash_form"]["option1"].value,
               choice2 : document.forms["dash_form"]["option2"].value,
               choice3 : document.forms["dash_form"]["option3"].value,
               csrfmiddlewaretoken : document.forms["dash_form"]["csrfmiddlewaretoken"].value
           },
           function(data,status)
           {
               window.location.href="/quiz/question/";
           }
       );
       }
 });