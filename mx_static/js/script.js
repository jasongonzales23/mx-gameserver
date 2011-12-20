/* Author: Jason Gonzales

*/

UTIL = {
 
  fire : function(func,funcname, args){
 
    var namespace = C10;  // indicate your obj literal namespace here
 
    funcname = (funcname === undefined) ? 'init' : funcname;
    if (func !== '' && namespace[func] && typeof namespace[func][funcname] == 'function'){
      namespace[func][funcname](args);
    } 
 
  }, 
 
  loadEvents : function(){
 
    var bodyId = document.body.id;
 
    // hit up common first.
    UTIL.fire('common');
 
    // do all the classes too.
    $.each(document.body.className.split(/\s+/),function(i,classnm){
      UTIL.fire(classnm);
      UTIL.fire(classnm,bodyId);
    });
 
    UTIL.fire('common','finalize');
 
  } 
 
};



C10 = {
    common : {
        init : function(){},
        finalize : function(){}
    },
    home : {
        init : function(){
            slideshow();
            },
        someID : function(){}
    },
    gallery : {
        init : function(){
        }
    }
}



// kick it all off here 
$(document).ready(UTIL.loadEvents);


//FUNCTIONS GET HOISTED
//need to make this generic 
function slideshow() {
    $('#slides').cycle({
        fx: 'fade',
        timeout: 5000,
        speed: 1000,
        prev: '.left-arrow',
        next: '.right-arrow'
    });
}
