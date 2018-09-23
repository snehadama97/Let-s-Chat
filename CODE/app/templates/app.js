var app = angular.module("app",[]);
app.controller("controller",function($scope,$http){


$http.get("./data.json").then(function(response){
$scope.Rishi=response.data;  //[{name:'Sneha',age:'19'},{name:'Dhwani',age:'20'}];
});

});
