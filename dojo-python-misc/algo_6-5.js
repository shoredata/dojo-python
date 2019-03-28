// CarFactory(make, model, color) ==> object

// CensorString(string, word) ==> string 

function CarFactory(make, model, color) {
    var retn = {};
    retn['make'] = make;
    retn['model'] = model;
    retn['color'] = color;   
    return retn; 
}
var car1 = CarFactory("Chevy", "Silverado", "Black");
console.log(car1);

function SubString(str, start, length) {
  var retn = "";
  for (var i=start; i<start+length; i++) {
    retn += str[i];    
  }
  // console.log(retn);
  return retn;
}
function ChrString(count,char) {
  var retn = "";
  for (var i=0; i<count; i++) {
    retn += char;    
  }
  return retn;
}
function CensorString(str,word) {
  retn = "";
  repl = ChrString(word.length, "*");
  // console.log(repl);
  for (i=0; i<str.length; i++) {
    teststr = SubString(str,i,word.length);
    if (teststr == word) {
      // console.log(teststr);
      retn += repl;
      i += word.length-1;
    }
    else{
      retn += str[i];
      // console.log(retn);
    }
  }
  return retn;
}
var source_string = "day.yad.Sunday is the shortest day of the week.day.d";
var target_string = "day";
console.log(source_string);
console.log(CensorString(source_string, target_string));

https://repl.it/@bearfish47x/js-algo-6-5

// OUTPUT:
// Native Browser JavaScript
// { make: 'Chevy', model: 'Silverado', color: 'Black' }
// day.yad.Sunday is the shortest day of the week.day.d
// ***.yad.Sun*** is the shortest *** of the week.***.d
// => undefined
   