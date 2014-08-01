var app = angular.module("nuvify", [])
	.controller("SongController", function($scope) {
        $scope.songs = {};
        $scope.songs.count = 1;
    } );

   app.controller('TagsCtrl', function($scope, $http) {
  	$http.get('http://localhost:8080/api/tags')
       .then(function(res){
          $scope.tags = res.data; 
          Console.log(res.data);               
        });
});