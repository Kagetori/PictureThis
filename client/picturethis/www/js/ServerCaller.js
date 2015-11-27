//Takes a custom url and parser. Then it calls the server using the url and gives the result to the parser

function serverCaller(api, params, parser, callback, exceptionHandler) {
    // IF you are testing on your VM, change the link to not have
    // HTTPS. Use HTTP only since the VM has no SSL certificate installed
    // eg var serverURL = "http://192.168.56.110/api/";
    var serverURL = "https://picturethis.brianchau.ca/api/";

    var isLoginCall = (api.substring(0, 6) == "login/");

    if (!isLoginCall) {
        params['auth_token'] = getUser().auth_token;
    }

    // This is the Client Version so the server can reject
    // calls from old clients
    params['client_version'] = 3;

    params['client_secret'] = "k8AwYC90MkUK2wsFZF36oCxe+cg+bIfMmHPWbFhLgObzGclWXKQhL/4vTCSOfzScV9QE0J6RYkxNmfMIhyi0mEfN+9o4AN8KCtfX3HJ8QpegztKFhit/d+O2d43xIe2r";

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
        if (xmlhttp.readyState == 4) {
            if (xmlhttp.status == 200) {
                // do something with the results
                if (xmlhttp.responseText != "undefined"){
                    debugAlert(xmlhttp.responseText);
                    var json_response = JSON.parse(xmlhttp.responseText);

                    if (json_response.hasOwnProperty('exception')) {
                        // Exception. If there is a specific callback, use the
                        // exceptionhandler to handle it. Otherwise use default exception
                        // handling of showing an alert

                        if (exceptionHandler) {
                            exceptionHandler();
                        } else {
                            showAlert(json_response.exception, '');
                        }

                        if (json_response.hasOwnProperty('force_logout') && json_response.force_logout && !isLoginCall) {
                            return;
                        }

                    } else {
                        hooks(json_response);

                        if (parser) parser(json_response);

                        if (callback) callback();
                    }

                    setSpinnerVisibility(false);
                }
            } else {
                showAlert("Server call failed. Please try again. Error " + xmlhttp.status, '');
                setSpinnerVisibility(false);
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
