'use strict';

var services = angular.module("vApp.services", []);

services.service("QAItemService", function($log, $localStorage){
	
//	var items = $localStorage.QAModel || [];
	
	$localStorage.$default({
		QAModel:[]
	});
	
	
	return {
		"all" : $localStorage.QAModel,
		"get": function(id){
			var elem = _.find($localStorage.QAModel, function(i){ return i.uid == id;});
			return elem;
		},
		"create" : function(item){
			
			item.uid = this.__newId__(); 
			item.created_date = new Date();
			$localStorage.QAModel.push(item);
			$log.debug("item created");
			
		},
		"update" : function(item){
			//write service to update existings record
			var elem = this.get(item.uid);
			angular.extend(elem, item);
			$log.debug("item updated");
		},
		"deleteItem" : function(id){
				var elem = this.get(id);
				$localStorage.QAModel.splice(_.indexOf($localStorage.QAModel, elem), 1);
			
			$log.debug("item deleted");
		},
		"__newId__": function(){ //returns unique id for primarykey of item
			return new Date().getTime(); 
		}
	
	}
	
	
});


services.service("VoteService", function($log, $localStorage){
	
	$localStorage.$default({
		VoteModal:[]
	});
	/*{
		uid: "unique id for vote",
		qaId:"asdsad",
		userId: "sdasd,
		value:"true/false"
	}
	*/
	
	return {
		create: function(item){
			item.uid = this.__newId__(); 
			item.created_date = new Date();
			$localStorage.VoteModal.push(item);
			$log.debug("item created");
		},
		getVotes4Question: function(qid){
			return _.filter($localStorage.VoteModal, function(item){
				return item.qaId == qid;
			});
		},
		getCount4Question: function(qid){
			return this.getVotes4Question(qid).length;
		},
		getYesCount4Question: function(qid){
			return _.filter($localStorage.VoteModal, function(item){
				return item.qaId == qid && item.value==true;
			}).length;
		},
		getNoCount4Question: function(qid){
			debugger;
			return _.filter($localStorage.VoteModal, function(item){
				return item.qaId == qid && item.value==false;
			}).length;
		},
		"__newId__": function(){ //returns unique id for primarykey of item
			return new Date().getTime(); 
		}
	}
	
});