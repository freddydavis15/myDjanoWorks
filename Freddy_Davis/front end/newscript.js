// task1

// var pound = prompt("enter the pounds");
// alert("the pounds :"+pound+" in kg is: " + pound*0.454);
// console.log("conversion completed");


// task2

// var firstName = prompt('enter your first name:');
// var lastName = prompt('enter your last name:');
// var age = prompt('enter your age:');
// var height = prompt('enter your height');
// var pet = prompt('enter your pet name:');
// alert('thank you for the informations')
// k=pet.length - 1
// if(firstName[0]===lastName[0] && age>20 && age<30 && height > 169)
// {
//   if(pet[k]==="y"||pet[k]==="Y")
//   {
//     console.log('welcome comrade');
//   }
//   else {
//     console.log('sorry, u have nothing here');
//   }
// }
// else {
//   console.log('sorry, u have nothing here');
// }


// task3

// function sleepin(weekday, vacation){
//   return (!weekday || vacation)
// }
//
// function monkeyTrouble(asmile, bsmile){
//   return(asmile && bsmile)||(!asmile && !bsmile)
// }
//
// function stringTimes(str,n){
//   var i=0;
//   var st="";
//   if (i<n){
//     st=st+str;
//     i++
//   }
// return st
// }
//
// function luckySum(a,b,c){
//   if(a===13){
//     return 0
//   }
//   else if (b==13) {
//     return a
//   }
//   else if (c==13) {
//     return a+b
//   }
//   else {
//     return a+b+c
//   }
// }
//
//
//
// function caught_speeding(speed, is_birthday){
//   if (is_birthday){
//     speed=speed-5;
//     if(speed<61){
//       result=0;
//     }
//     else if (speed<81 && speed>60) {
//       result=1;
//     }
//     else {
//       result=2;
//     }
//   }
//   else {
//     if(speed<61){
//       result=0;
//     }
//     else if (speed<81 && speed>60) {
//       result=1;
//     }
//     else {
//       result=2;
//     }
//   }
// }

// function makeBricks(small,big,goal) {
//   return goal%5 >=0 && goal%5 -small <=0 && big*5 +small >= goal;
// }






// task4
// var flag=true;
// var list=[]
// while (flag) {
//   var sel = prompt("select an action:\n add,remove,display,quit");
//   if (sel==="add"){
//     var name = prompt("enter a name");
//     list.push(name);
//   }
//   else if (sel==="remove") {
//     var name = prompt("enter a name");
//     var res=list.indexOf(name);
//     if(res<0){
//       alert("no such name")
//     }
//     else {
//       list.splice(res,1)
//     }
//   }
//   else if (sel==="display") {
//     list.forEach(alert);
//   }
//   else if (sel==="quit") {
//     flag=false
//   }
// }


// task5

var employee={
  name: "john smith",
  job: "Programmer",
  age:"31",
  nameLength: function(){
    console.log(this.name.length);
  }
}


var employee={
  name: "john smith",
  job: "Programmer",
  age:"31",
  nameLength: function(){
    alert("Name is"+this.name+"job is "+this.job+"age is "+this.age);
  }
}

var employee= {
  name: "john smith",
  job: "Programmer",
  age: "31",
  lastName:function(){
    list1=this.name.split(" ")
    k=list1.length()
    console.log(list1[k]);
  }
}
