const BASE_URL="http://20.55.39.17:1337",showRegister=()=>{$(".login").hide(200),$(".register").show(200)},showLogin=()=>{$(".register").hide(200),$(".login").show(200)},getFormData=i=>{var t=i.serializeArray(),n={};return $.map(t,function(i,t){n[i.name]=i.value}),n},login=i=>{window.api.send("login",i)};$("form").on("submit",async function(e){e.preventDefault();var inputs,url,req=await fetch(BASE_URL+$(this).attr("action"),{method:"POST",body:JSON.stringify(getFormData($(this))),headers:{"content-type":"application/json"}}),res=await req.json();200==req.status?(pushSuccessNotify("DisLaugh",res.message),res.action&&eval(res.action)):pushErrorNotify("DisLaugh",res.message)}),$(".ctrl-btn-exit").on("click",function(){window.api.send("exit")}),$(".ctrl-btn-min").on("click",function(){window.api.send("minimize")}),$(".ctrl-btn-max").on("click",function(){window.api.send("maximize")});