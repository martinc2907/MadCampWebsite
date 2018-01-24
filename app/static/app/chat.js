$('#chat-form').on('submit',function(event){
	event.preventDefault();

	$.ajax({
		url: 'post',
		type: 'POST',
		data: { msgbox:  $('input[name = "chat-msg"]').val() },

		success: function(json){

			$('#chat-msg').val('');
			$('#msg-list').append('<li class="text-right list-group-item" style= "background-color: antiquewhite" >' + json.msg + '</li>');
			var charlist = document.getElementById('msg-list-div');
			charlist.scroolTop = charlist.scrollHeight;
		}
	})
});


function getMessages(){
	if(!scrolling){
		//Get all chat objects from database, and display them. 
		$.get('messages', function(messages){
			$('#msg-list').html(messages);
			var chatlist = document.getElementById('msg-list-div');
			chatlist.scrollTop = chatlist.scrollHeight;
		});
	}
	scrolling = false;
}

var scrolling = false;
$(function(){
	$('#msg-list-div').on('scroll', function(){
		scrolling = true;
	});
	refreshTimer = setInterval(getMessages, 500);
});


// For disabled send button.
$(document).ready(function(){
	$('#send').attr('disabled','disabled');
	$('#chat-msg').keyup(function(){
		if($(this).val()!= ''){
			$('#send').removeAttr('disabled');
		}
		else{
			$('#send').attr('disabled', 'disabled');
		}
	});
});



//From the django docs-- replacing csrf token in html
// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});