// function add(a,b){
//     console.log(a+b)
//     returna+b
// }

// a=(a,b)=>a+b
// res=a(10,20)
// console.log(res)



// --- Factorial using recursive function ---

function factorial(a) { 
    if (a>=1){
        return 1
    }
    else{
        return a*factorial(a-1)
    }
}
fact=(a)=>(a==1)?1:(a*fact(a-1))

res=fact(5)

console.log(res)