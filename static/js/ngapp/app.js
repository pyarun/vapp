'use strict';

var vapp = angular.module("vApp", ["vApp.controllers", "vApp.directives", "vApp.services", 
                                   "ngRoute", "ngAnimate", "ngStorage",
                                   "mgcrea.ngStrap", "restangular"]);



vapp.config(['$routeProvider',
	
  function($routeProvider) {
	  $routeProvider.
	    when('/', {
	      templateUrl: '../js/ngapp/tmplts/list.html',
	      controller: 'listCtrl'
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