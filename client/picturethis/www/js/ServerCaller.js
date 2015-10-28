//Takes a custom url and parser. Then it calls the server using the url and gives the result to the parser
var ServerCaller = function(url,parser) {
    var emptyFunction = function() {};
    var serverCaller = new ServerCaller(url,parser,emptyFunction);
};

var ServerCaller = function(url,parser,callback) {
    showAlert("called ServerCaller!");
    var xmlhttp;
    if (window.XMLHttpRequest){
        xmlhttp = new XMLHttpRequest();
        if ( typeof xmlhttp.overrideMimeType != 'undefined') {
            xmlhttp.overrideMimeType('application/json');
        }
    }
    else {
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }

    xmlhttp.open('GET', url, true);
    xmlhttp.send();

    xmlhttp.onreadystatechange = function() {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            // do something with the results
            if (xmlhttp.responseText != "undefined"){
                showAlert(xmlhttp.responseText);
                parser(xmlhttp.responseText);
                callback();
                }
        } else {
            // wait for the call to complete
        };
    };
}