var request = require('request');
var files = require('fs');

for (i=0; i < 7; i++) {
    var startTime = Date.now();
    var startDate = new Date(startTime);
    var endTime = new Date(Date.now()).setDate(startDate.getDate()+i);
    var endDate = new Date(endTime);
    var html = "";
    var country = 'us';
    var city = 'Boston';
    var category_id = '1';
    var state = 'MA';
    var key = '1743c52773e172746156c60174f2964'
    var url = 'https://api.meetup.com/2/concierge?key='+ key +'&sign=true&photo-host=public&country='+ country +'&city='+ city +'&category_id='+ category_id +'&state='+ state +'time=' + startTime + ',' + endTime;

    request(url, function(err,res,body)
    {
        if (err) {
            err = err;
        }
        else {
            var events = JSON.parse(body).results;
            html = "<li>" + startDate + "\n";
            for (i = 0; i < events.length; i++)
            {
                var event = events[i];
                html += event.name + "\n";
                if (typeof(event.venue) != "undefined" && event.venue)
                {
                   html += event.venue.city +  ", " + event.venue.address_1 +  "\n"; 
                }
                html += event.description + "\n\n";
            }
            html += "</li>";
        }
        files.writeFileSync("result.html", html);
    })
}