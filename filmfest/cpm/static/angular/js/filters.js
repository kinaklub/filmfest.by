'use strict';

/* Filters */

angular.module('filmfestApp.filters', []).
  filter('interpolate', ['version', function(version) {
    return function(text) {
      return String(text).replace(/\%VERSION\%/mg, version);
    }
  }]);
/*
angular.module('filmfestApp.filters', []).
    filter('id', function () {
        console.log('idfilter call');
        return function (id) {
            var idNumber = parseInt(id, 10);

            return idNumber;
        }
    } );
  */