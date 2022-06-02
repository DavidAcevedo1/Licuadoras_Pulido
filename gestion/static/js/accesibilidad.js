let classes = ["f0", "f1", "f2", "f3", "f4", "f5", "f6"];
let classIndex = 2;

document.getElementById('aumentar').addEventListener('click', ()=>{
    let previousClass = classIndex;
    classIndex = classIndex + 1;
    classIndex = (classIndex== classes.length) ? classes.length - 1: classIndex;
    changeClass(previousClass, classIndex ); 
});

document.getElementById('disminuir').addEventListener('click', ()=>{
    let previousClass = classIndex;
    classIndex = classIndex - 1;
    classIndex = (classIndex < 0) ? 0 : classIndex;
    changeClass(previousClass, classIndex);
});
document.getElementById('restaurar').addEventListener('click', ()=>{
    let previousClass = classIndex;
    html.classList.toggle('dark-mode');
    changeClass(previousClass, 2);
});

let changeClass = (previous, next)=>{
    if(previous != next){
        let htmlElement = document.querySelector('html');
        htmlElement.classList.remove(classes[previous]);
        htmlElement.classList.add(classes[next]);
    }
}
changeClass()
const boton = document.getElementById('dark');
const html = document.admin-body.html;
boton.addEventListener('click', ()=>{
    html.classList.toggle('dark-mode');
});