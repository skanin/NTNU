/* Lager referanser til HTML elementer */
let inpItem = document.getElementById("inpItem");
let ol = document.getElementsByTagName("ol")[0];
let completed = 0;
let update = document.getElementById("update");
let itemList = document.getElementById("itemList");

/* Lager en tom array, som skal inneholde alt som brukeren legger til*/
let tasks = [];


function isChecked() {
    /* Funksjonen sjekker om checkboxen er checked eller ikke. Oppdaterer "completed" variablen, og lager listen på nytt*/
    let index = event.target.id;  //Finner id'en til den checkboxen som ble klikket (som også er dens plass i arrayet tasks)
    if(!tasks[index].checked){
        completed += 1;
        tasks[index].checked = true;  //Setter "checked" til true i objektet i arrayet.
    }else{
        completed -= 1;
        tasks[index].checked = false;
    }

    drawList();
}

function addTask() {
    //Funksjon for å legge til tasks. Finner først tiden den ble lagt til, deretter legger til en objekt i arrayet tasks og til slutt tegner opp listen
    let d = new Date();
    let n = d.getTime();
    let task = {Time: n, Task: inpItem.value, checked: false};
    tasks.push(task);
    console.log(tasks);
    drawList();
}

function drawList() {
    /*Funksjon som tegner opp listen med elementene i tasks arrayet. Lager elementer av type "li", "input" og "label" og appender disse til
    HTMLen. Oppdaterer også span elementet som viser hvor mange som er completed.
     */
    itemList.innerHTML = '';

    for (let task of tasks) {
        let li = document.createElement("li");
        let checkbox = document.createElement('input');
        let label = document.createElement("label");
        checkbox.setAttribute('type', 'checkbox');
        checkbox.setAttribute('id', tasks.indexOf(task));
        checkbox.addEventListener('click', isChecked);

        label.innerHTML = task.Task;

        if (task.checked) {
            checkbox.setAttribute('checked', true);
        }
        li.appendChild(checkbox);
        li.appendChild(label);
        ol.insertBefore(li, ol.firstChild);
    }
    let numbTasks = tasks.length;
    update.innerHTML = completed + "/" + numbTasks + " completed";
}

inpItem.onkeydown = function (evt) {
    //Hvis brukeren har klikket inne i input-elementet og deretter klikker enter, vil tasken bli lagt til.
  if(evt.keyCode === 13 ){
      addTask();
  }
};