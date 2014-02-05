var app = angular.module("Task", []).config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});;

app.controller("TaskCtrl", function ($http) {
    var app = this;

    $http.get('/api/task').success(function (data) {
        app.tasks = data.objects;
    });
});