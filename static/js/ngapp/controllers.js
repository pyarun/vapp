'use strict';

var controllers = angular.module("vApp.controllers", []);

controllers.controller("AddCampaignCtrl", ["$scope", "$log", "QAItemService", "$alert",
                                           function($scope, $log, QAItemService, $alert){
	$scope.show=false;
	$scope.showerrors = false;
	
	$scope.saveItem = function(){
		$scope.show=true;
		if($scope.addItemForm.$valid){
			QAItemService.create($scope.item);
			$log.debug("item saved");
			$alert({
			  "content": "Item Added",
			  "type": "success",
			  "placement":"top-right",
			  "data-container" : "body",
			  "duration" : "3"
			});
			$scope.item = {};
		}else{
			$scope.showerrors=true;
		}
		$scope.show=false;
	};
	
	$scope.saveItemAsDraft = function(){
		$log.debug("item drafted");	
	};
	
	
}]);


controllers.controller("listCtrl", ["$scope", "QAItemService", "$modal", "VoteService",
                                    function($scope, QAItemService, $modal, VoteService){
	$scope.allItems = QAItemService.all;
	
	/*deletes a item from list*/
	$scope.remove = function(id){
		QAItemService.deleteItem(id);
	}
	
	/*model form for voting*/
	var voteModal = $modal({
		scope: $scope,
		title: "Add your opinion",
		template: '../js/ngapp/tmplts/voteModal.html', show: false,
		contentTemplate:'../js/ngapp/tmplts/voteModalContent.html'});
	
	/*show modal for voting*/
	$scope.openVoteModal=function(item){
		$scope.item = item;
		voteModal.$promise.then(voteModal.show);
	};
	
	/*save user vote*/
	$scope.addVote = function(item, dismiss){
		var vote = {
				userId: new Date().getTime(),
				qaId: item.uid,
				value:item.vote
		};
		VoteService.create(vote);
		dismiss();
	};
	
	/*model form for voting*/
	var viewVotesModal = $modal({
		scope: $scope,
		title: "View Votes", show:false,
		contentTemplate:'../js/ngapp/tmplts/viewVotesContent.html'});
	
	/*allows to view user votes in modal box*/
	$scope.viewVotes = function(item){
		$scope.data ={
				allvotesforquestion : VoteService.getVotes4Question(item.uid),
				total : VoteService.getCount4Question(item.uid),
				yes : VoteService.getYesCount4Question(item.uid),
				no : VoteService.getNoCount4Question(item.uid)
		};
		viewVotesModal.$promise.then(viewVotesModal.show);
	}
	
}]);

controllers.controller('EditItemCtrl', ["$scope", "$routeParams", "QAItemService", "$log", "$alert",
                                        function($scope, $routeParams, QAItemService, $log, $alert){
	var item = _.find(QAItemService.all, function(i){ return i.uid == $routeParams.itemId;});
	$scope.item = angular.copy(item);
	$scope.editingMode=true;
	
	$scope.updateItem = function(){
		$scope.show=true;
		if($scope.addItemForm.$valid){
			QAItemService.update($scope.item);
			$log.debug("item updated");
			$alert({
			  "content": "Item Updated",
			  "type": "success",
			  "placement":"top-right",
			  "data-container" : "body",
			  "duration" : "3"
			});
			$scope.item = {};
		}else{
			$scope.showerrors=true;
		}
		$scope.show=false;
	};
	
}]);

