var PictureThisService = function() {

    this.initialize = function() {
        // No Initialization required
        var deferred = $.Deferred();
        deferred.resolve();
        return deferred.promise();
    }

    this.user = new User(null, null, null, null, null, null);
	
}
