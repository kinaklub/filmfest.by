'use strict';

/* Services */


// Demonstrate how to register services
// In this case it is a simple value service.
angular.module('filmfestApp.services', []).
  value('version', '0.1');

var filmfestServices = angular.module('filmfestServices', ['ngResource']);

filmfestServices.factory('Submission', ['$resource',
    function($resource) {
        return $resource('/ru/2014/api/submissions/:submId/', {}, {
            query: {
                method: 'GET',
                params: {format: 'json'},
                isArray: true
            }
        })
    }])
