var gulp        = require('gulp');
var browserSync = require('browser-sync').create();
var sass        = require('gulp-sass');
// var countdown = require('jquery-countdown');

// Define default destination folder
var dest = 'static/themes';

// Compile sass into CSS & auto-inject into browsers
gulp.task('bootstrap-css', function() {
    return gulp.src(['node_modules/bootstrap/scss/bootstrap.scss', dest +'/scss/*.scss'])
        .pipe(sass())
        .pipe(gulp.dest(dest + "/css/bootstrap"))
        .pipe(browserSync.stream());
});

// Move the javascript files into our /src/js folder
gulp.task('bootstrap-js', function() {
    return gulp.src(
        [
            'node_modules/bootstrap/dist/js/bootstrap.min.js',
            'node_modules/jquery/dist/jquery.slim.min.js',
            'node_modules/jquery/dist/jquery.min.js',
            'node_modules/tether/dist/js/tether.min.js',
            'node_modules/popper.js/dist/umd/popper.min.js',
            'node_modules/jquery-countdown/dist/jquery.countdown.js'
        ])
        .pipe(gulp.dest(dest + "/js/bootsrap"))
        .pipe(browserSync.stream());
});

// Static Server + watching scss/html files
gulp.task('serve', ['bootstrap-css'], function() {

    browserSync.init({
        server: './' + dest + '/scss'
    });

    gulp.watch(
        [
            'node_modules/bootstrap/scss/bootstrap.scss',
            'themes/static/themes/scss/*.scss',
            'themes/static/themes/default/*.scss'
        ], [
            'bootstrap-css'
        ]);
    gulp.watch("./templates/*.html").on('change', browserSync.reload);
});

gulp.task('default', ['bootstrap-js','serve']);
gulp.task('production', ['bootstrap-js','bootstrap-css']);
