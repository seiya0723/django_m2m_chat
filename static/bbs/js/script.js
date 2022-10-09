window.addEventListener("load" , function (){

    //イベントをセットする要素が動的に変化する場合、documentからイベントを指定する
    $(document).on("click","#message_submit", function(){ message_submit(); });
    $(document).on("click",".chat_area_button", function(){ chat_area(this.value); });

});

function chat_area(url){

    let method  = "GET";

    $.ajax({
        url: url,
        type: method,
        dataType: 'json'
    }).done( function(data, status, xhr ) {

        if (data.error){
            console.log("ERROR");
        }
        else{
            $("#chat_area").html(data.content);
        }

    }).fail( function(xhr, status, error) {
        console.log(status + ":" + error );
    });

}


function message_submit(){


    let form_elem   = "#form_area";

    let data    = new FormData( $(form_elem).get(0) );
    let url     = $(form_elem).prop("action");
    let method  = $(form_elem).prop("method");

    $.ajax({
        url: url,
        type: method,
        data: data,
        processData: false,
        contentType: false,
        dataType: 'json'
    }).done( function(data, status, xhr ) {

        if (data.error){
            console.log("ERROR");
        }
        else{
            $("#message_area").html(data.content);
            $("#textarea").val("");
        }

    }).fail( function(xhr, status, error) {
        console.log(status + ":" + error );
    });

}
