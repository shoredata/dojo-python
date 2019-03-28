function arraysZip(arr1, arr2) {
    var newobj = {};
    for (var i=0; i<arr1.length; i++) {
      newobj[arr1[i]] = arr2[i];
    }
    return newobj;
  }
  testa = ['fruit', 'veg', 'meat']
  testb = ['apple', 'tomato', 'beef']
  console.log(testa + " + " + testb + " ==> ")
  console.dir(arraysZip(testa,testb))
  
  function reverseString(str) {
    newstr = ""
    for (var idx = str.length-1; idx>=0; idx--) {
      newstr += str[idx];
    }
    return newstr
  }
  function isPalindrome(str) {
    return reverseString(str)==str;
  }
  function isPalindrome2(str) {
    for (var i=0; i< Math.floor(str.length/2); i++) {
      if (str[i] != str[str.length-1-i]) {
        return false;
      }
    }
    return true;
  }
  test1 = "abba"
  test2="rabbit"
  console.log(test1 + " (strcopy)" + isPalindrome(test1))
  console.log(test2 + " (strcopy)" + isPalindrome(test2))
  console.log(test1 + " (inplace)" + isPalindrome2(test1))
  console.log(test2 + " (inplace)" + isPalindrome2(test2))
  
  // OUTPUT:
  // Native Browser JavaScript
  // fruit,veg,meat + apple,tomato,beef ==>
  // { fruit: 'apple', veg: 'tomato', meat: 'beef' }
  // abba (strcopy)true
  // rabbit (strcopy)false
  // abba (inplace)true
  // rabbit (inplace)false
  // => undefined
  //