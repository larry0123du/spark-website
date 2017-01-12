$(document).ready(function() {
	$("a").click(function(){
		var pos = $(this).attr("id");
		pos = parseInt(pos);
		if (pos != 0) {
			var offset = pos * $(window).height();
			$("body").stop(true).animate({
				scrollTop: offset + 'px'
			}, 1500);
		}
		else {}
	});

});