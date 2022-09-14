let total = 0;
document.querySelectorAll('#total_venta').forEach(datos_venta=>{
    total += parseFloat(datos_venta.textContent)
})
document.getElementById('total_campos').textContent = total
