(function(){
    if (window.bookmarklet !== undefined){
        bookmarklet();
    }
    else {
        document.body.appendChild(document.createElement('script')).src='https://imarks.herokuapp.com/static/js/bookmarklet.js?r='+Math.floor(Math.random()*99999999999999999999);
    }
})();