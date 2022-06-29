def total_carrito(request):
    total = 0 
    for key, value in request.session["carrito"].items():
        total=total+float(value["precio"])
    return {"total_carrito": total}
