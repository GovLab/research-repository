$(document).ready(function() {
	$(document).foundation();

  // Off Canvas Menu
  $('.e-mainnav-trigger').click(function() {
  	var trigger = $(this);
  	console.log(trigger);

  	if(trigger.hasClass('m-nav-active')) {
  		trigger.removeClass('m-nav-active');
	  	trigger.parent().removeClass('m-nav-active');	
  	} else {
  		trigger.addClass('m-nav-active');
	  	trigger.parent().addClass('m-nav-active');	
  	}

  });

$('#overlay').click(function() {
	$(this).removeClass('m-active');
	$('.b-filters').removeClass('m-active');
});

// RSS from Digest
$('#blog-container').rssfeed('http://thegovlab.org/researchrepo/feed/', 
  { 
    limit: 10,
    linktarget: '_blank',
    content: true,
    media: true
  });

$('#digest-container').rssfeed('http://thegovlab.org/govlab-digest/feed/',
  {
    limit: 10,
    linktarget: '_blank',
    content: true,
    media: true
  });


 }); // Closes Document.ready

        