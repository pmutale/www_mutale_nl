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
var plugins = require("gulp-load-plugins")({
    pattern: ['gulp-*', 'gulp.*', 'main-bower-files'],
    replaceString: /\bgulp[\-.]/
});
var mainBowerFiles = require('main-bower-files');
var concat = require('gulp-concat');
var rename = require('gulp-rename');
var filter = require('gulp-filter');
var flatten = require('gulp-flatten');
var notify = require('gulp-notify');
var sourcemaps = require('gulp-sourcemaps');


// Define default destination folder
var dest = 'styles/';
var bower_components = 'styles/bower_components';
var raw = 'static/raw';

// BowerFiles JS
gulp.task('bower-components', function () {
    var jsFilter = filter('**/*.js', {restore: 'true'});
    var cssFilter = filter('**/*.css', {restore: 'true'});
    var fontFilter = filter(['*.eot', '*.woff', '*.svg', '*.ttf'], {restore: 'true'});
    var imageFilter = filter(['*.gif', '*.png', '*.svg', '*.jpg', '*.jpeg'], {restore: 'true'});

    return gulp.src(mainBowerFiles(), {base: bower_components })
    // JS
        .pipe(jsFilter)
        .pipe(gulp.dest(dest + '/libs/js'))
        .pipe(concat('_main.js'))
        .pipe(uglify({compress:true}))
        .pipe(gulp.dest(dest + '/libs/js'))
        .pipe(jsFilter.restore)
        .pipe(notify({ message: 'Bower JS task complete' }))

        // CSS
        .pipe(cssFilter)
        .pipe(sourcemaps.init())
        .pipe(gulp.dest(dest + '/libs/css'))
        .pipe(concat('_main.css'))
        .pipe(gulpIf('*.css', cssnano()))
        .pipe(gulp.dest(dest + '/libs/css'))
        .pipe(cssFilter.restore)
        .pipe(notify({ message: 'Bower CSS task complete' }))

        //FONTS
        .pipe(fontFilter)
        .pipe(flatten())
        .pipe(gulp.dest(dest + '/libs/fonts'))
        .pipe(fontFilter.restore)
        .pipe(notify({ message: 'Bower Fonts task complete' }))

        // IMAGES
        .pipe(imageFilter)
        .pipe(flatten())
        .pipe(gulp.dest(dest + '/libs/images'))
        .pipe(imageFilter.restore)
        .pipe(notify({ message: 'Bower Images task complete' }))

});

//SASS
gulp.task('sass', function(){
    return gulp.src('styles/scss/**/*.scss')
        .pipe(sourcemaps.init())
        .pipe(sass()) // Converts Sass to CSS with gulp-sass
        .pipe(gulp.dest('static/raw/css'))
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
});


//Production
gulp.task('heroku:production',function (callback){
    runSequence( 'clean:static', 'sass', 'bower-components',
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
