var app = angular.module("nuvify", [])
	.controller("SongController", function($scope) {
        $scope.songs = {};
        $scope.songs.count = 1;
    } );