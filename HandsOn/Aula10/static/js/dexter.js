$(document).ready(function(){

    $("#enviar").click(function(){
        var app_name = $("#app-name").val();
        var desenv_list = $("#desenv-list").val();
        var comandos = $("#comandos").val();

        var data = "{\"app\":\""+app_name+"\", \
                      \"desenvolvedores\":\""+desenv_list+"\", \
                      \"comandos\":\""+comandos+"\"}";

        $.ajax({
            type: "POST",
            url: "/api/dexterops/",
            contentType:"application/json",
            data:JSON.stringify(data)

        })
        .done(function(data){
            alert(data.message);
        })

        .fail(function(data){
            alert(data.message);
            console.log(data);


        })
    });


})