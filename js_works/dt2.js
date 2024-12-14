// a=[1,2,3,"apple"]
// console.log(a[3])
// console.log(a[-2])
// a[2]=100
// a[4]=100
// a[7]=100
// console.log(a.length)


// a.push(100)
// res=a.pop()
// res=a.join(" ")
// console.log(a)
// console.log(res)


// res=a.slice(1,3)
// console.log(res)


// delete a[2]
// console.log(a)

// shift
// unshift
// concat




// a=[1,2,3,21,7,35,70,4]
// for(i of a){
//   console.log(i**2)
// }
// --
// sq=(val)=>console.log(val**2)
// a.forEach(sq)
// --
// a.forEach((val)=>console.log(val**2))


// >>> FACTORIAL <<<
// fact=(item)=>{
//     if(item==1){
//         return 1
//     }
//     else{
//         return item*fact(item-1)
//     }
// }
// res=fact(5)
// console.log(res)

// fact=(item)=>(item==1)?1:(item*fact(item-1))
// console.log(fact(3))


// a=[1,2,3,21,7,35,70,4]
// fact=(item)=>(item==1)?1:(item*fact(item-1))
// a.forEach((item)=>console.log((item==1)?1:(item*fact(item-1))))


// a=[1,2,3,21,7,35,70,4]
// a.forEach(item=>console.log(item**2))
// res=a.map((item)=>item**2)
// console.log(res)


// a=[1,2,3,21,7,35,70,4]
// res=a.map((item)=>(item==1)?1:(item*fact(item-1)))
// console.log(res)


// names=["ajith","amal","harikrishnan","joy","anu"]
// res=names.map((item)=>(item.length))
// console.log(res)



// a=[1,2,3,12,45,33,97,96,85,61]
// res=a.filter((item)=>item%2==0)
// console.log(res)


// a=[1,2,3,12,45,33,97,96,85,61]
// res=a.find(item=>item==33)
// console.log(res)


// a=[1,2,3,12,45,33,97,96,85,61]
// // res=a.reduce((total,item)=>total+item)
// // console.log(res)
// // -
// res=a.reduce((total,item)=>total>item?total:item)
// console.log(res)



// names=["ajith","amal","harikrishnan","joy","anu"]
// names.sort()
// names.reverse()
// console.log(names)


// a=[21,3,45,89,1,23,17,97,8]
// // a.sort((a,b)=>a-b)
// a.sort((a,b)=>b-a)
// console.log(a)


a=[21,3,45,89,1,23,17,97,8]
// res=a.every(item=>item>0)
res=a.every(item=>item>0)
console.log(res)