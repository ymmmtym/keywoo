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

// nav
$(function(){
	$('.navbar-toggler').click(function(){
		$(this).next('div').slideToggle();
  });
});

// all check
$(function() {
  // 1. 「全選択」する
  $('#all').on('click', function() {
    $("input[name='check']").prop('checked', this.checked);
  });
  // 2. 「全選択」以外のチェックボックスがクリックされたら、
  $("input[name='check']").on('click', function() {
    if ($('#boxes :checked').length == $('#boxes :input').length) {
      // 全てのチェックボックスにチェックが入っていたら、「全選択」 = checked
      $('#all').prop('checked', true);
    } else {
      // 1つでもチェックが入っていたら、「全選択」 = checked
      $('#all').prop('checked', false);
    }
  });
});