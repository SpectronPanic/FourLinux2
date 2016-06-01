$(function(){
    $("#novo-provisionamento").click(function(){
        var repo = $("#repositorio").val();
        var desenvolvedores = $("#desenvolvedores").val();
        var job = $("#job").val();
        var branches = $("#branches").val();
        var containers_domain = $(".container-domain").val();

        var json = '{"_id":1,
                     "gitlab":{"repo":"'+repo+'","desenvolvedores":"'+desenvolvedores+'"},
                     "jenkins":{"job":"'+job+'","branches":"'+branches+'"},
                     "docker":"'+containers_domain+'"}';

        $.ajax({
            url: "/provisionamento/novo/",
            type: "POST",
            dataType: "json",
            contentType:"application/json; charset=utf-8",
            data: JSON.stringify(json),
        })
        .done(function(data){
            console.log(data.message);
        })
        .fail(function(data){
            console.log(data.message);
        })
        
    });

});
