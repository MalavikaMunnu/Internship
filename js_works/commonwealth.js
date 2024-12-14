commonwealth=[
    {country:"India",gold:21,silver:13,bronze:12},
    {country:"USA",gold:10,silver:10,bronze:9},
    {country:"China",gold:2,silver:2,bronze:22},
    {country:"Russia",gold:16,silver:22,bronze:2},
    {country:"South Korea",gold:11,silver:10,bronze:7},
]
// --->>> display every names of countries who participated in commonwealth
// commonwealth.forEach(item=>console.log(item.country))

// --->>> display names of every countries who have more than 15 gold medals
// res=commonwealth.filter((item)=>item.gold>15)
// res.forEach(item=>console.log(item.country))
//                     // OR
// commonwealth.filter((item)=>item.gold>15).forEach(item=>console.log(item.country))

// --->>> ind the total number of silver medals won by every country
// res=commonwealth.map((item)=>item.silver).reduce((total,item)=>(total+item))
// console.log(res)


// --->>> display names of countries in ascending order of their bronze count
// commonwealth.sort((a,b)=>a.bronze-b.bronze)
// commonwealth.forEach(item=>console.log(item.country))


// --->>> display the medal details of country India
// ind=commonwealth.find(item=>item.country=="India")
// console.log(ind)


// --->>> find the country with least number of gold medels
res=commonwealth.reduce((total,item)=>total.gold>item.gold?item:total)
console.log(res)