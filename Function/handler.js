const rest = require('restler')
const event_key = "cweKjQyxdRO2yzwCWFSvL"

function bin2string(array){
    var result = "";
    for(var i = 0; i < array.length; ++i){
        result += (String.fromCharCode(array[i]));
    }
    return result;
}

exports.handler = function(context, event) {
    var event_parsed = JSON.parse(JSON.stringify(event));
    var message = bin2string(event_parsed.body.data);
	var message_obj = JSON.parse(message);
    let device_name = event_parsed.url.split("/")[2];
	if (message_obj.current_temperature > message_obj.max_temperature) {
		rest.post('https://maker.ifttt.com/trigger/high_temperature/with/key/' + event_key, {data: {value1: message_obj.current_temperature, value2: device_name}}).on('complete', function(data){
			console.log(device_name + " - Current Temperature: " + message_obj.current_temperature + "°C");
		});
	}
    context.callback("");
};