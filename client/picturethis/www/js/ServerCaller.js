//Takes a custom url and parser. Then it calls the server using the url and gives the result to the parser

function serverCaller(api, params, parser, callback, unusedParam) {
    var serverURL = "http://picturethis.brianchau.ca/api/";

    if (api.substring(0, 6) != "login/") {
        params['auth_token'] = getUser().auth_token;
    }

    debugAlert("called ServerCaller!");
    var xmlhttp;
    if (window.XMLHttpRequest){
        xmlhttp = new XMLHttpRequest();
        if ( typeof xmlhttp.overrideMimeType != 'undefined') {
            xmlhttp.overrideMimeType('application/json');
        }
    } else {
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }

    xmlhttp.open('POST', serverURL + api, true);

    xmlhttp.onreadystatechange = function() {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            // do something with the results
            if (xmlhttp.responseText != "undefined"){
                debugAlert(xmlhttp.responseText);
                parser(xmlhttp.responseText);
                if (callback) callback();
            }
        } else {
            // wait for the call to complete
        }
    };

    var formData = new FormData();

    for (var key in params) {
        if (params.hasOwnProperty(key)) {
            formData.append(key, params[key]);
        }
    }

    xmlhttp.send(formData);
}
