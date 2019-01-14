/*
Im using "Const" for declaring variables that are constant, and "let" for variables that changes it's values. 
For example: Const logo = document.getElementById("logo");, because this is constant.
for(let i = 0; i<9; i++){}, the variable I is changing value for each time the for loop runs, therefore I'm using "let"
 */

/* Part 2 */
console.log('PART 2'); //Logs "PART 2" to the console

for(let i = 1; i<21; i++){ //As long as i < 21, it logs the value of i to the console. I updates every time the loops restarts.
  console.log(i);
}

/* Part 3 */
console.log('PART 3'); //Logs "PART 3" to the console.

const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]; //Array of numbers
for(let i = 0; i<numbers.length; i++){
    /*The loop loops through the array, the ampunt of times equal to the length of the array
    * If the i index of the array i gives a rest of 0 when divided by 3, it should print "eple"
    * If it gives a rest of 0 when divided by 5, it should print "kake"
    * If it gives a rest of 0 when divided by 3 and divided by 5, it should print "eplekake".
    * Else it should print the number located at the i index.
    * */
    if(numbers[i]%3 === 0 && numbers[i]%5 === 0){
        console.log("eplekake");
    } else if(numbers[i]%3 === 0){
        console.log("eple");
    } else if (numbers[i]%5 === 0){
        console.log("kake");
    } else{
        console.log(numbers[i]);
    }
}
/* Part 4 */
const title = document.getElementById("title");  //Getting the HTML element with ID = "title"
title.innerHTML = "Hello, JavaScript";  //Changes the innerHTML of title to "Hello, JavaScript".

/* Part 5 */
const hidden = document.getElementById("hidden");  //Getting the HTML elements with ID = "hidden" and ID = "magic"
const magic = document.getElementById("magic");


//Each of these three functions is added to the desired buttons' onclick in the HTML
function changeDisplay(){  //Function that changes the display style of magic to "none".
    magic.style.display = "none";
}

function changeVisibility(){  //Function that changes the visibility style of magic to "hidden"
    magic.style.visibility = "hidden";
}

function reset(){  //Function that changes the display style and visibility style of magic to "block" and "visible".
    magic.style.display = "block";
    magic.style.visibility = "visible";
}

/* Part 6 */
const technologies = [  //Array of technologies
  'HTML5',
  'CSS3',
  'JavaScript',
  'Python',
  'Java',
  'AJAX',
  'JSON',
  'React',
  'Angular',
  'Bootstrap',
  'Node.js'
];
const tech = document.getElementById("tech"); //Getting the HTML element with id = "tech".
for (let i = 0; i<technologies.length; i++){
    /*For loop that loops the amount of times equal to technologies length.
    * Each time it loops, it should add the item at this i index of technologies to tech's innrHTML, wrapped with <li> tags
    * */
    tech.innerHTML += "<li>" + technologies[i] + "</li>";
}