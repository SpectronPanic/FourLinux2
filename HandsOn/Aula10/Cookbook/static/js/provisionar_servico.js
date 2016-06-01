$(function(){

    $("#provisionar").click(function(){
        var application = $("#application").val();
        var repo = $("#repo").val();
        var developers = $("#developers").val();
        var commands = $("#commands").val();

        $.ajax({
            type:"post",
            url:'/provisionar/',
            contentType: "application/json",
            data: JSON.stringify('{"application":"'+application+'", \
                                    "repo":"'+repo+'", \
                                    "developers":"'+developers+'", \
                                    "commands":"'+commands+'"}')

        })
        .done(function(data){
            alert("Enviado com Sucesso!");
        })
        .fail(function(data){
            alert("Falhou ao provisionar servico");
        })



    });


});
