
var img = document.createElement('img');
img.src = './static/b5.png';
img.id = 'captcha'
var canvas = document.createElement('canvas');
var context = canvas.getContext("2d");
context.drawImage(img, 0,0);
var imgData = context.getImageData(0,0,img.width/6, img.height);

var preddict_button = document.createElement('button');
preddict_button.textContent = 'Preddict';

var body = document.getElementsByTagName('body')[0];
body.appendChild(img);
body.appendChild(preddict_button);

const x = tf.browser.fromPixels(imgData);
// const prediction = model.predict(imgData);

let model;
(async function() {
    model = await tf.loadLayersModel('./static/jsmodel/model.json')
})();

