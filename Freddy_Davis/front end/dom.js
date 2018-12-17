var hover=document.querySelector('#one')
var click=document.querySelector('#two')
var dclick=document.querySelector('#three')

hover.addEventListener('mouseover',function() {
hover.textContent = "ohh something happened";
hover.style.color='red';
})

hover.addEventListener('mouseout',function() {
hover.textContent = "hover me";
hover.style.color='black';
})


click.addEventListener('click',function() {
click.textContent = "CLicked me";
click.style.color='red';
})

dclick.addEventListener('dblclick',function() {
dclick.textContent = "double clicked ";
dclick.style.color='red';
})
