(function(){
    if (window.bookmarklet !== undefined){
        bookmarklet();
    }
    else {
        document.body.appendChild(document.createElement('script')).src='https://imarksbucket.s3.amazonaws.com/static/js/bookmarklet.js?r='+Math.floor(Math.random()*99999999999999999999);
    }
})();