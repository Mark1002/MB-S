function file_upload_model(fileupload) {
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
            var image_container = select_image_container();
            var image = $("<img>").attr({
                "src": data.result.image_url,
                "width": 50,
                "height": 50,
            }).addClass("img-thumbnail");
            if(image_container.find("img").length === 0) {
                image_container.empty();
            }
            image_container.append(image);
            console.log(image_container);
        }
    });
}

function select_image_container() {
    var image_container = $("#prediction-upload").find(".image-container");
    return image_container;
}

$(function(){
    $("#prediction-upload .upload-image").click(function() {
        var fileupload = $(this).parent().find("input[type='file']");
        console.log(fileupload);
        $(".progress-bar").css({"width": "0%"});
        $(".progress-bar").text("0%");
        file_upload_model(fileupload, "predict_image");
    });    
});
