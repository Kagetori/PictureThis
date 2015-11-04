//Takes a custom url and parser. Then it calls the server using the url and gives the result to the parser
var ServerCaller = function(api,params,parser) {
    var emptyFunction = function() {};
    var serverCaller = new ServerCaller(api,params,parser,emptyFunction);
};

var ServerCaller = function(api,params,parser,callback) {
    var serverURL = "http://picturethis.brianchau.ca/api/";

    if (api.substring(0, 6) != "login/") {
        var authToken = getUser().auth_token;

        params += "&auth_token=" + encodeURIComponent(authToken);
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
    xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

    xmlhttp.onreadystatechange = function() {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            // do something with the results
            if (xmlhttp.responseText != "undefined"){
                showAlert(xmlhttp.responseText);
                parser(xmlhttp.responseText);
                if (callback) callback();
            }
        } else {
            // wait for the call to complete
        }
    };

    xmlhttp.send(params);
}
