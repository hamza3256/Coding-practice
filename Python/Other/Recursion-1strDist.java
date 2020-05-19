public int strDist(String str, String sub) {
  if(str.indexOf(sub) == -1){
    return 0;
  }
  if(str.length() < sub.length()){
    return sub.length();
  }
  if(str.startsWith(sub) && str.endsWith(sub)){
    return str.length();
  }else if(str.startsWith(sub)) {
   return strDist(str.substring(0, str.length()-1), sub);
  }else{
    return strDist(str.substring(1), sub);
  }
}
