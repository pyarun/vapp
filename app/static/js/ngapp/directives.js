'use strict';

var directives = angular.module("vApp.directives", []);

/** directive to add ajax loader image */
directives.directive("ajaxLoader", [function(){
	return {
		template:'<i ng-show="show" class="loadingimg"></i>',
		replace:true,
		scope:{
			show:"=",
			size:"@"
		}
	};
}]);