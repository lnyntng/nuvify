var app = angular.module("nuvify", []);

app.controller("SongController", function($scope) {
    $scope.songs = {};
    $scope.songs.count = 1;
});
