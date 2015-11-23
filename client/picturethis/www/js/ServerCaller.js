//Takes a custom url and parser. Then it calls the server using the url and gives the result to the parser

function serverCaller(api, params, parser, callback, unusedParam) {
    // there is this unusedParam; all calls to serverCaller currently
    // send null to this. If you ever need to send a new param to serverCaller,
    // you can change the name of this and use it.

    // IF you are testing on your VM, change the link to not have
    // HTTPS. Use HTTP only since the VM has no SSL certificate installed
    // eg var serverURL = "http://192.168.56.110/api/";
    var serverURL = "https://picturethis.brianchau.ca/api/";

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
                var json_response = JSON.parse(xmlhttp.responseText);

                if ((typeof json_response.force_logout != "undefined") && (json_response.force_logout)) {
                    showAlert(json_response.exception, "Logging out");
                    logout();
                    return;
                }

                if (parser) parser(json_response);

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
