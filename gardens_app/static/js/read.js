$(document).ready(function() {
    var $rssDiv = $('#newRssFeed');
    var allKeywords = {};

    var allEntries = [];
    var urlsLoaded = [];


// django docs, https://docs.djangoproject.com/en/1.7/ref/contrib/csrf/
// cookies/

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
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




// add a rss/
    function getRssFeed () {

        function googleApiCall(urls) {
            google.load("feeds", "1", {
                callback: init(urls)
            });

            function init(urls) {
                for (var i = 0; i < urls.length; i++) {
                    console.log(i);
                    urlsLoaded[i] = false;
                    loadFeed({
                        url: urls[i].feedUrl,
                        indx: i,
                        noOfFeed: 4
                    })
                }
            }
        }

        $.ajax({
            url: '/view_rss/',
            type: 'GET',
            success: function (res) {
                console.log(res);
                googleApiCall(res);
            },
            error: function (e) {
                console.log(e);
            }
        });
    }

    function displayRssForm() {
        $rssDiv.html(
                '<div><button id="addRss" class="btn btn-info">Add a rss</button></div>'+
                '<input class="form-control" type="text" id="newRssInput">   <span class="input-group-btn">'
        );

        $('#addRss').click(function() {
            var newUrl = $('#newRssInput').val();
            console.log(newUrl);
            addNewRssFeed(newUrl);
        })
    }


    function addNewRssFeed(url) {
        var newUrl = JSON.stringify(url);
        $.ajax({
            url: '/add_rss/',
            type: 'POST',
            dataType: 'json',
            data: newUrl,
            success: function (res) {
                console.log(res);
            },
            error: function (e) {
                console.log('post not working');
                console.log(e);
            }
        })
        $('#allMyRss').click(function () {
            $rssDiv.html('');
            getRssFeed();
            console.log('final: ', allEntries);
        });

        $("#addRss").on('click', function() {
            displayRssForm();
            addNewRssFeed();
        });
    });
})