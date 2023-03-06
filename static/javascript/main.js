// using a jquery selector to save these elements as variables
const user_input = $("#user-input")
const search_icon = $('#search-icon')
const cities_div = $('#replaceable-content')
// connecting it to the cities.html with the url path ''	
const endpoint = ''
const delay_by_in_ms = 100
let scheduled_function = false

let ajax_call = function (endpoint, request_parameters) {
	// sends an Ajax request to the end point with the parameters 
	$.getJSON(endpoint, request_parameters)
		.done(response => {
			// fade out the div, then:
			cities_div.fadeTo('slow', 0).promise().then(() => {
				// replace the HTML contents
				cities_div.html(response['html_from_view'])
				// fade-in the div with new contents
				cities_div.fadeTo('slow', 1)
			})
		})
}


// when a user types this function is called
user_input.on('keyup', function () {

	const request_parameters = {
		q: $(this).val() // value of user_input: the HTML element with ID user-input
	}

	// if scheduled_function is NOT false, cancel the execution of the function
	if (scheduled_function) {
		clearTimeout(scheduled_function)
	}

	// setTimeout returns the ID of the function to be executed
	// we do this because if we don't have a delay the database could be flooded by requests
	scheduled_function = setTimeout(ajax_call, delay_by_in_ms, endpoint, request_parameters)
})