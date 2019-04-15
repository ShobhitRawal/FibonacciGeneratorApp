var myApp = angular.module('myApp', []);
myApp.controller("myCtrl", function ($scope, $http) {

$scope.number;
$scope.nthNumber;
$scope.showDiv = false;

$scope.findNumber = function () {
$scope.start_time = new Date().getTime();
$scope.url = "https://myfibonacciapp.herokuapp.com/fibonacci/"+String($scope.number)+"/";

$http(
{
method: 'GET',
url: $scope.url
}).then(function (response)
{
   $scope.showDiv = true;
   $scope.nthNumber = response.data.nth_number;
   $scope.end_time = new Date().getTime();
   $scope.total_time = ($scope.end_time - $scope.start_time);
   $scope.total_time=$scope.total_time/1000;

});



}


});
