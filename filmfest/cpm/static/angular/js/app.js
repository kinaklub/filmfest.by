'use strict';


$(function () {
    angular.module('filmfestApp', [
            'ngRoute',
            'filmfestControllers',
            'filmfestServices',
            'solo.table'
        ]).
        config(['$routeProvider', function ($routeProvider) {
                $routeProvider.when('/downloading_films', {
                    templateUrl: window.FILMFEST_PATH + 'partials/downloading_films.html',
                    controller: 'SimpleSubmissionsList'});
                $routeProvider.when('/edit/:submId', {
                    templateUrl: window.FILMFEST_PATH + 'partials/edit_submission.html',
                    controller: 'EditSubmissionCtrl'
                });
                $routeProvider.otherwise({
                    redirectTo: '/downloading_films'
                });
        }]).
        config([
        '$interpolateProvider',
            function($interpolateProvider){
                $interpolateProvider.startSymbol('<[');
                $interpolateProvider.endSymbol(']>');
            }
        ]);

    angular.bootstrap(document, ['filmfestApp']);
});

// Declare app level module which depends on filters, and services
var map = {
    "comments": {
        "comment":"textarea",
        "comment_email_sent":"checkbox",
        "comment_film_received":"checkbox",
        "comment_papers_received":"checkbox",
        "comment_vob_received":"checkbox"
    },
    "dates": {
        "submitted_at":"date",
        "email_sent_at":"date",
        "film_received_at":"date",
        "papers_received_at":"date",
        "vob_received_at":"date",
        "updated": "date" // readonly , last update
    },
    "film_info": {
        "id":"input",
        "title":"input",
        "title_en":"input",
        "country":"select",
        "language":"select",
        "genre":"input", //should be multi select
        "section":"select", //
        "synopsis":"textarea",
        "length":"input", //digit
        "aspect_ratio":"input",
        "year":"input",
        "premiere":"select",
        "film_awards":"Лучший игровой фильм 2012 года (Всероссийский фестиваль \"REC\")",
        "director_awards":"\"Собеседник\" - Лучший игровой фильм 2012 года (Всероссийский фестиваль \"REC\")\n\"Человек один\" - Лучший игровой фильм 2012 года (Международный фестиваль \"Петербургский экран\" и всероссийский - \"Бумеранг\")",
        "budget":"1 проезд на трамвае",
        "film_link":"http://files.mail.ru/FE2F115610784F879444C578C06801CF",
        "attend":"No",
        "backlink":"vk.com"
    }
}

