'use strict';

var vapp = angular.module("vApp", ["vApp.controllers", "vApp.directives", "vApp.services", 
                                   "ngRoute", "ngAnimate", "ngStorage",
                                   "mgcrea.ngStrap", "restangular", "directive.g+signin"]);



vapp.config(['$routeProvider',
	
  function($routeProvider) {
	  $routeProvider.
	    when('/', {
	      templateUrl: '../js/ngapp/tmplts/list.html',
	      controller: 'listCtrl',
	      data:{
	      	login_required:true,
		      permission_required:true
	      }
	      
	    }).
	    when('/add', {
	      templateUrl: '../js/ngapp/tmplts/add.html',
	      controller: 'AddCampaignCtrl'
	    }).
	    when('/edit/:itemId',{
	    	templateUrl: '../js/ngapp/tmplts/add.html',
	    	controller: 'EditItemCtrl'
	    }).
	    otherwise({
	      redirectTo: '/add'
	    });
}]);


vapp.run(function ($rootScope, AuthService) {
  /*$rootScope.$on('$routeChangeStart', function (event, next) {
    if(next.data.login_required){
    	if( ! AuthService.isAuthenticated()) {
    		event.preventDefault();
    		location.href="http://google.com";
    	}
    }
    if(next.data.permission_required){
    	
    }
  	var authorizedRoles = next.data.authorizedRoles;
    if (!AuthService.isAuthorized(authorizedRoles)) {
      event.preventDefault();
      if (AuthService.isAuthenticated()) {
        // user is not allowed
        $rootScope.$broadcast(AUTH_EVENTS.notAuthorized);
      } else {
        // user is not logged in
        $rootScope.$broadcast(AUTH_EVENTS.notAuthenticated);
      }
    }
  });*/
})