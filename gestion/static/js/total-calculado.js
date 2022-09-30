let numbers = [];

document.querySelectorAll('#totaldetalle').forEach(item=>{
    numbers.push(parseInt( item.textContent))
})
let total = numbers.reduce((a, b) => a + b, 0);
console.log(total)
document.getElementById('total-calculado');
let resultado = document.getElementById('total-calculado');

resultado.textContent = total