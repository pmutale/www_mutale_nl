/* jshint node:true, strict:false */

var gulp = require('gulp');
var sass = require('gulp-sass');
var browserSync = require('browser-sync').create();
var useref = require('gulp-useref');
var uglify = require('gulp-uglify');
var gulpIf = require('gulp-if');
var cssnano = require('gulp-cssnano');
var imagemin = require('gulp-imagemin');
var runSequence = require('run-sequence');
var del = require('del');
// var plugins = require("gulp-load-plugins")({
//     pattern: ['gulp-*', 'gulp.*', 'main-bower-files'],
//     replaceString: /\bgulp[\-.]/
// });
// var mainBowerFiles = require('main-bower-files');
var concat = require('gulp-concat');
// var rename = require('gulp-rename');
// var filter = require('gulp-filter');
// var flatten = require('gulp-flatten');
var notify = require('gulp-notify');
var sourcemaps = require('gulp-sourcemaps');


// Define default destination folder
var dest = 'static/themes';
// var bower_components = 'static/styles/bower_components';
// var raw = 'static/raw';


// Compile Bootstrap into css
gulp.task('bootstrap', function() {
    return gulp.src(['node_modules/bootstrap/scss/bootstrap.scss', 'src/scss/*.scss'])
        .pipe(sass())
        .pipe(gulp.dest(dest + "/css/bootstrap"))
        .pipe(browserSync.stream());
});

gulp.task('js', function() {
    return gulp.src(['node_modules/bootstrap/dist/js/bootstrap.min.js', 'node_modules/jquery/dist/jquery.min.js', 'node_modules/tether/dist/js/tether.min.js'])
        .pipe(gulp.dest("static/js/bootstrap"))
        .pipe(browserSync.stream());
});
//SASS
gulp.task('sass', function(){
    return gulp.src('styles/scss/**/*.scss')
        .pipe(sourcemaps.init())
        .pipe(sass()) // Converts Sass to CSS with gulp-sass
        .pipe(gulp.dest('static/css/raw'))
        .pipe(browserSync.reload({
            stream:true
        }))
        .pipe(notify({ message: 'Bower SASS task complete' }))
});


//Minify JS
gulp.task('useref-js', function () {
    return gulp.src('styles/js/**/*.js')
        .pipe(useref())
        .pipe(concat('main.min.js'))
        .pipe(gulpIf('*.js', uglify()))
        .pipe(gulp.dest(dest + 'js'))
        .pipe(notify({ message: 'Bower JS task complete' }))
});


//Minify CSS
gulp.task('useref-css', function () {
    return gulp.src('static/raw/css/**/*.css')
        .pipe(useref())
        .pipe(concat('main.min.css'))
        .pipe(gulpIf('*.css', cssnano()))
        .pipe(gulp.dest(dest + 'css'))
        .pipe(notify({ message: 'Bower CSS task complete' }))
});


//Optimise Images
gulp.task('images', function(){
    return gulp.src('styles/img/**/*.+(png|jpg|jpeg|gif|svg)')
        .pipe(imagemin({
            interlaced: true
        }))
        .pipe(gulp.dest('static/themes/img/'))
});


//Fonts
gulp.task('fonts', function() {
    return gulp.src('styles/fonts')
        .pipe(gulp.dest(dest))
        .pipe(notify({ message: 'Bower Fonts task complete' }))
});


//Cleaning Up
gulp.task('clean:static', function() {
    return del.sync('static/');
});

gulp.task('clean:raw', function() {
    return del.sync('static/raw');
});

gulp.task('clean:bower', function() {
    return del.sync('styles/bower_components');
});




//BrowserSync
gulp.task('browserSync', function () {
    browserSync.init({
        server: {
            baseDir: './styles'
        }
    })
});

// Watch
gulp.task('watch', ['browserSync', 'sass'], function () {
    gulp.watch('styles/scss**/*.scss', ['sass']);
    gulp.watch('styles/scss/main.scss', ['sass']);
    gulp.watch('styles/img/**/*', ['images']);
    gulp.watch('app/templates/**/*.html', browserSync.reload);
    gulp.watch('styles/js/**/*.js', browserSync.reload);
    gulp.watch('styles/css/**/*.css', browserSync.reload);
    gulp.watch('styles/static/js/**/*.js', browserSync.reload);
    gulp.watch('styles/static/css/**/*.css', browserSync.reload);
    gulp.watch(['node_modules/bootstrap/scss/bootstrap.scss', 'src/scss/*.scss'], ['sass']);
});


//Production
gulp.task('heroku:production',function (callback){
    runSequence( 'clean:static', 'sass',
        ['useref-js', 'useref-css', 'images', 'fonts'],  'clean:raw', 'clean:bower',
        callback);
    console.log('Building static files... You can have a cup of tea!!');
});


// Default
gulp.task('default', function (callback) {
    runSequence(['sass','browserSync', 'watch'],
        callback
    )
});
