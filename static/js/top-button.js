var btn = $('#button');
var nav = $('#navbarfixed');

$(window).scroll(function() {
  if ($(window).scrollTop() > 300) {
    btn.addClass('show');
  } else {
    btn.removeClass('show');
  }
});

btn.on('click', function(e) {
  e.preventDefault();
  $('html, body').animate({scrollTop:0}, '300');
});


$(window).scroll(function() {
  if ($(window).scrollTop() > 150) {
    nav.addClass('shadow');
  } else {
    nav.removeClass('shadow');
  }
});
