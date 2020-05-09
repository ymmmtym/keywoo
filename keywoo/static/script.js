// get link for other port
function jumpport(port) {
    location.href ='http://' + location.hostname + ':' + port;
    return false;
}

// check if form is blank
function check_blank(text,name){
  if(text.elements[name].value==""){
    return false;
  }
}

// fade in contents
$(document).ready(function(){
  $('body').fadeIn('slow');
});