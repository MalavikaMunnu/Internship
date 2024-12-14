// class Student{
//     constructor(){
//         name="Ajith"
//         age=20
//         display(){
//             console.log("Hello")
//         }
//     }
// }
// s1=new Student()
// console.log(s1.name)
// console.log(s1.age)
// s1.display()


// class Student{
//     constructor(){
//         this.name=n
//         this.age=a
//     }
//     display(){
//         console.log('name:$(this.name),age:$(this.age)')
//     }
// }
// s1=new Student()
// s1.display()






class School{
    sc_name="ppptttmmm"
}
class Student extends School{
    name="Ajith"
}
s1=new Student()
console.log(s1.sc_name)



baleno={
    manufacturer:"Suzuki",
    fuel:"petrol",
    color:"black",
    transmission:["manual","amt"]
}

glanza={
    manufacturer:"Toyota",
}

glanza.__proto__=baleno
console.log(glanza.color)
console.log(glanza.fuel)
console.log(glanza.transmission)
console.log(glanza.manufacturer)