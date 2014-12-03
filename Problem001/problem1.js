var set = Array.apply(null, Array(1000)).map(function (_, i) {return i + 1;});
var total = 0;
for( x in set ){
	if( ( ( set[ x ] % 3 == 0 ) || ( set[ x ] % 5 == 0 ) ) && set[ x ] < 1000 ){
		total += set[x];
	}
}
console.log( total );
