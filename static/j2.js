
var img = document.createElement('img');
img.src = './static/b5.png';
img.id = 'captcha';
var dataURL;
var message = {};
var serverData;

img.onload = function () {
    var canvas = document.createElement('canvas');
    var context = canvas.getContext("2d");
    context.drawImage(img, 0, 0);
    dataURL = canvas.toDataURL();
    dataURL = dataURL.replace('data:image/png;base64,', '');
    // console.log(dataURL);
    message['image'] = dataURL;

    var post_button = document.createElement('button');
    post_button.textContent = 'Predict';
    post_button.id = 'predict';
    body.appendChild(post_button);

    $("button#predict").click(function () {
        $.post('/api', JSON.stringify(message),
            function (data, status) {
                console.log(data["answer"]);
                serverData = data;
            });
    });
};

var body = document.getElementsByTagName('body')[0];
body.appendChild(img);

