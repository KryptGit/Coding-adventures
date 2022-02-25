let square_Hieght = 20
let sq_speed = 1
function setup() {
  createCanvas(400, 740);
  Button = createButton('jump');
  
  
}

function draw() {
  background(220);
  square(30, square_Hieght, 55);
  while (square_Hieght > 0){
    square_Hieght += sq_speed;
    return false
  }



}
