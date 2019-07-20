function jumpport(port) {
    location.href ='http://' + location.hostname + ':' + port;
    return false;
}

function check_blank(text){
  if(text.elements["search"].value==""){
    return false;
  }
}
