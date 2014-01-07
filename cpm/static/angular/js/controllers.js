'use strict';

/* Controllers */

var filmfestControllers = angular.module('filmfestControllers', []);

filmfestControllers.controller('SimpleSubmissionsList', [ '$scope', '$http', '$filter',
    function($scope, $http, $filter) {
    var parseSubmissionJson = function (json) {
        var len, i, current, curProp,
            convertToInt = [
                'id',
                'length',
                'year'
            ],
            convertToBoolean = [
                'comment_email_sent',
                'comment_film_received',
                'comment_papers_received'
            ];

        var parseBoolean = function (string) {

            if (string.toLowerCase !== undefined) {

                string = string.toLowerCase();
                if (string === 'true') {
                    return true;
                } else {
                    return false;
                }
            } else {
                return false;
            }

            return Boolean(string);
        }

        for (i = 0, len = json.length; i < len; i++) {
            current = json[i];

            _.each(convertToInt, function(prop) {
                curProp = current[prop];
                if (curProp !== undefined) {
                    current[prop] = parseInt(current[prop], 10);
                }

            });

            _.each(convertToBoolean, function (prop) {
                curProp = current[prop];
                if (curProp !== undefined) {
                    current[prop] = parseBoolean(current[prop]);
                }
            });
        }
        return json;
    }
    $scope.submissions = [];
//    console.log(window.FILMFEST_PATH + 'submissions/submissions.json');
//    $http
//        .get(window.FILMFEST_PATH + 'submissions/submissions.json')
//        .success(function(data) {
//        console.log('subms number', data.length);
//        //$scope.submissions = parseSubmissionJson(data);
//    });
//   console.log('submissions', $scope.submissions);
    $scope.filterSubmissions = function () {
        var parseRecieved = function (string) {
            string = string.toLowerCase();
            if (string === 'true') {
                return true;
            }

            return Boolean(string);
        };
                            $scope.filterSubmissions
        var isFiltered = function(subm, query) {
            var propertyMap = {
                'id':'id',
                'received': 'comment_film_received'
                },
                result = true, queryId, queryReceived;

            var searchReceived = function () {

                if (query.received === undefined || query.received === '' || query.received === 'all') {
                    return true;
                }

                queryReceived = query.received === 'true' ? true : false;

                if (subm['comment_film_received'] === queryReceived) {
                    return true;
                }

                return false;
            };

            var searchById = function () {
                    if (query.id === undefined || query.id === '' ) {
                        return true;
                    }

                    if ( parseInt($scope.query.id, 10)  === parseInt(subm.id, 10) ) {
                        return true;
                    }

                    return false;
            }


           if (searchById() && searchReceived()) {
               result = true;
           } else {
               result = false;
           }

            return result;
        };


        return function (subm) {
            var query = $scope.query;

            if (query === undefined || query === '') {
                return true;
            }

            if (isFiltered(subm, query)) {
                return true;
            }
        }
    }

    $scope.searchById = function () {
            return function (subm) {
                if ($scope.query === undefined || $scope.query === '') {
                    return true;
                }

                if ( parseInt($scope.query.id, 10)  === parseInt(subm.id, 10) ) {
                    return true;
                }

                return false;
            }
    }

    $scope.query = {};
    $scope.query.received = 'all';
    $scope.editSubm = { id: 0}
    $scope.editSubmId = {id: 0}


    $scope.editSubmission = function (ev) {
        console.log('edit submission');
        console.log(ev.target);
        var id = parseInt($(ev.target).closest('tr').find('.download_films_id').text(), 10)
        $scope.editSubmId.id = id;
        debugger;
        $scope.editSubm = $filter('filter')($scope.submissions, $scope.editSubmId);

        $('#edit_submission').modal();
    }
}]);

filmfestControllers.controller('EditSubmissionCtrl', [
'$scope',
'$routeParams',
'Submission'
, function($scope, $routeParams, Submission) {
    $scope.submId = $routeParams.submId;

    $scope.subm = Submission.get({submId: $routeParams.submId},
                                 function(subm) {
                                     console.log(subm);
                                 })

}]);


