var MX = MX || {};

MX.answersArr = [];
MX.scoresArr = [];

MX.qrChallenge = function (options){
    var scanned = options.code,
    message = options.successMsg,
    showAnswer = options.displaySuccessAnswer,
    showScore = options.displaySuccessScore,
    score, answer;
    
    for (key in options.codeValuePairs){
        if(scanned === options.codeValuePairs[key].qrCode){
            score = options.codeValuePairs[key].value;
            answer = options.codeValuePairs[key].qrCode;
        }
    }
    //save the score
    MX.storeAnswer(options.questionNumber, answer, score);
    MX.printAnswer(message, answer, score, showAnswer, showScore);
};

MX.textChallenge = function (options){
    $('body').delegate('.save', 'click', function(){
        var processAnswer = function(){
            var answer = $.trim($('#textAnswer').val()),
            possibleScore = options.score,
            score = 0,
            closeAnswers = options.closeAnswers;
            
            if(answer===options.correctAnswer){
                score = possibleScore;
            }
            //loop through close answers
            else {
                for (key in closeAnswers){
                    if(answer === closeAnswers[key]){
                        score = possibleScore; 
                    }
                }
            }
            MX.storeAnswer(options.questionNumber, answer, score);
        }
        
        if(options.confirmation){
            MX.dialog({
                prompt:options.confirmationPrompt,
                cancelCallback: function(){
                    return;
                },
                confirmCallback: function(){
                    processAnswer(options);
                }
            });
            
        }
        else{
            processAnswer(options);
        }
    });
}

MX.numberChallenge = function(options){
    var $input = $('#numberAnswer');
    $('body').delegate('.save', 'click', function(){
        var processAnswer = function(){
            possibleScore = options.score,
            score = 0,
            correctAnswer = parseInt(options.correctAnswer),
            range = parseInt(options.range),
            high = correctAnswer + range,
            low = correctAnswer - range;
            
            if(answer===correctAnswer){
                score = possibleScore;
            }
            //loop through close answers
            else {
                if(answer >= low && answer <= high){
                    score = possibleScore; 
                }
            }
            MX.storeAnswer(options.questionNumber, answer, score);
        };
            
        var answer = parseInt($input.val(), 10);
        if(isNaN(answer)){
            MX.alertBox({prompt:options.alertMessage});
            $input.val('');
            return;
        }
        else{
            if(options.confirmation){
                MX.dialog({
                    prompt:options.confirmationPrompt,
                    cancelCallback: function(){
                        $input.val('');
                        return;
                    },
                    confirmCallback: function(){
                        processAnswer(options);
                    }
                });
            }
        }
    });
};

MX.printAnswer = function(message, answer, score, showAnswer, showScore){
    $('#results').remove();
    $('#scanner').before('<p id="results">' + message + '</p>');
    if(showAnswer){
        $('#results').append(' '+ answer + '. ');
    }
    if(showScore){
        $('#results').append('You scored ' + score + ' points.');
    }
    $('#results').hide().show(300);
}


MX.hiddenElements = function(options){
    $('body').delegate('.showEl', 'click', function(){
        $('#hiddenElement').addClass('reveal');
    });
    $('body').delegate('.hideEl', 'click', function(){
        $('#hiddenElement').removeClass('reveal');
    });
    
    console.log(options);
    
    if(options){
        var img = options.pathToHiddenElement,
        buttonText = options.buttonText;
        $('#hiddenElement').append('<img src="' + img + '"/>');
        $('#hiddenElement').append('<button class="hideEl">Close</button>');
        $('.challengeText').last().after('<button class="showEl">'+ buttonText + '</button>');
    }
}

MX.crossDomainPost = function (url) {
// Add the iframe with a unique name
    var iframe = document.createElement("iframe");
    var uniqueString = "BILLY_BILLY_BILLY";
    document.body.appendChild(iframe);
    iframe.style.display = "none";
    iframe.contentWindow.name = uniqueString;
    
    // construct a form with hidden inputs, targeting the iframe
    var form = document.createElement("form");
    form.target = uniqueString;
    form.action = "http://"+ url +"/teamData/";
    form.method = "GET";
    
    // repeat for each parameter
    for (var i=0; i<localStorage.length; i++){
        var key=localStorage.key(i);
        if(key !== "url") {
            var input = document.createElement("input");
            input.type = "hidden";
            input.name = key;
            input.value = localStorage.getItem(key);
            form.appendChild(input);
        }
    }
    //faker
    document.body.appendChild(form);
    $(form).submit();
}
        
function printLocalStorage(){
    $('#displaystuff').empty();
        for (var i=0; i<localStorage.length; i++){
            var key = localStorage.key(i);
            var value = localStorage.getItem(key);
            if( key !== "url" ) {
                $('#displaystuff').append('<p>' + key + ': ' + value + '</p>');
            }
        }
}
        
        
function clearLocal(){
    //remove everything from localStorage expect the IP
    $('#displaystuff').empty();
    for (var i=0; i<localStorage.length; i++){
        var key = localStorage.key(i);
        if( key !== "url" ) {
            localStorage.removeItem(key)
        }
    }
}

MX.storeAnswer = function(questionNumber, answer, score){
    //check if any answers
    var Qs = MX.constants.numberOfQuestions,
    questionIndex = questionNumber -1,
    answers  = localStorage.getItem('answers'),
    scores = localStorage.getItem('scores');
    //if not make placeholders for all the questions (still nee do test this)
    if(!answers){
        for(i=0; i<Qs; i++){
            MX.answersArr.push(' ');
        }
       localStorage.setItem('answers', MX.answersArr);
    }
    
    if(!scores){
        for(i=0; i<Qs; i++){
            MX.scoresArr.push(' ');
        }
       localStorage.setItem('scores', MX.scoresArr);
    }
   
    //now get the answers
    var answerStore = localStorage.getItem('answers');
    //turn the answers into an array
    answerStore = answerStore.split(',');
    //set the question answered to the correct value
    answerStore[questionIndex] = answer;
    //store the answers array
    localStorage.setItem('answers', answerStore);
    
    var scoreStore = localStorage.getItem('scores');
    scoreStore = scoreStore.split(',');
    scoreStore[questionIndex] = score;
    localStorage.setItem('scores', scoreStore);
}



MX.dialog = function (options) {
    $('body').append('<div id="blanket"></div>').hide().fadeIn(300);
    $('<form id="prompt" class="clearfix" action=""><label for="code-input">' + options.prompt + '</label><a href="#" id="cancel">No</a><a href="#" id="affirm">Yes</a></form>').appendTo(document.body).fadeIn();

    $('#prompt').delegate('#cancel', 'click', function(e) {
        e.preventDefault();
        $('#prompt').fadeOut().remove();
        $('#blanket').fadeOut().remove();
        options.cancelCallback();
    });

    $('#prompt').delegate('#affirm', 'click', function(e) {
        e.preventDefault();
        $('#prompt').fadeOut().remove();
        $('#blanket').fadeOut().remove();
        options.confirmCallback();
    });
}

MX.alertBox = function (options) {
    $('body').append('<div id="blanket"></div>').hide().fadeIn(300);
    $('<form id="alert" class="clearfix" action=""><label for="code-input">' + options.prompt + '</label><a href="#" id="cancel">OK</a></form>').appendTo(document.body).fadeIn();
    $('#alert').delegate('#cancel', 'click', function(e) {
        e.preventDefault();
        $('#alert').fadeOut().remove();
        $('#blanket').fadeOut().remove();
    });

} 