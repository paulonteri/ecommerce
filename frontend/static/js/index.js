var hiddenBox = $( "#red" );

console.log(hiddenBox);

$( "#button-container button" ).on( "click", function( event ) {
    hiddenBox.css('color', 'red');
});

