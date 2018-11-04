function file_upload_model(fileupload, context) {
    fileupload.click();
    fileupload.fileupload({
        dataType: 'json',
        sequentialUploads: true,
        start: function(e) {
            $('#modal-progress').modal({
                backdrop: 'static',
                keyboard: false
            });
        },
        stop: function(e) {
            $('#modal-progress').modal('hide');
        },
        progressall: function (e, data) {
            var progress = parseInt(data.loaded / data.total * 100, 10);
            var strProgress = progress + "%";
            $(".progress-bar").css({"width": strProgress});
            $(".progress-bar").text(strProgress);
        },
        done: function (e, data) {
            console.log(data.result);
            var image_container = select_image_container(context, $(this));
            var image = $("<img>").attr({
                "src": data.result.image_url,
                "width": 50,
                "height": 50,
            }).addClass("img-thumbnail");
            if(image_container.find("img").length === 0) {
                image_container.empty();
            }
            if(context == "predict_image") {
                image_container.empty();
            } 
            image_container.append(image);
            console.log(image_container);
        }
    });
}

function select_image_container(context, context_obj) {
    var image_container = null;
    switch(context) {
        case "image_class":
            image_container = context_obj.parents("tr").find(".image-container");
        break;
        case "predict_image":
            image_container = $("#prediction-upload").find(".image-container");
        break;
    }
    return image_container;
}

function reset_progress_bar() {
    $(".progress-bar").css({"width": "0%"});
    $(".progress-bar").text("0%");
}

$(function(){
    $("#image-class-upload .upload-image").click(function(){
        reset_progress_bar()
        var fileupload = $(this).parent().find("input[type='file']");
        console.log(fileupload);
        file_upload_model(fileupload, "image_class");
    });
    $("#prediction-upload .upload-image").click(function() {
        reset_progress_bar()
        var fileupload = $(this).parent().find("input[type='file']");
        console.log(fileupload);
        file_upload_model(fileupload, "predict_image");
    });
    $("#train-model").click(function() {
        var challenge_id = $("input[name='challenge_id']").val();
        var csrf_token = $("input[name='challenge_id']").attr('csrfmiddlewaretoken');
        console.log(csrf_token);
        
        $.ajax({
            url: "/model-training/",
            method: "post",
            data: {challenge_id: challenge_id, csrfmiddlewaretoken: csrf_token},
            dataType: 'json',
        }).done(function(res) {
            console.log(res);
            $("#training-message").css("display", "block");
        });
    });
    (function poll(){
        setTimeout(function() {
            $.ajax({ 
                url: "/model-training/polling/", 
                dataType: "json"
            }).done(function(data){
                var isTrain = data.is_train_finish;
                if (isTrain) {
                    console.log("train finish!!");
                    $('#training-finish').modal();
                }
            }).always(poll);
        }, 5000);
    })();    
});
