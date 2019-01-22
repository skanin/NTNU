let tax = document.getElementById("tax");
let wealth = document.getElementById("wealth");
let income = document.getElementById("income");


function taxFun() {
    tax.value = (0.35 * income.value) + (0.25 * wealth.value);
}
