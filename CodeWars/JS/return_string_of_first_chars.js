function makeString(s){
    var result = '';
    
    for (w of s.split(' ')){
        result += w[0];
    }
    
    return result;
