
console.log("ankitkumar")

function fun(){
	console.log("ankit");
}

function GetDetails(rest_id){
	let xhr = new XMLHttpRequest();
	let url = 'restuarant/' + rest_id;
	xhr.open('GET', url, true);
	xhr.onload = function(){
		fetchdetails(this.responseText, rest_id);
	};
	xhr.send();
}

function fetchdetails(data, rest_id){
	data = json.parse(data);
	let table_body = "";
	for(dish in data){
		table_body +=
		`<tr>
		<td>${dish['dish_name']}</td>
		<td>${dish['dish_price']}</td>
		<td>
                   
                <select class="form-control offset-md-3 col-md-6 col-sm-12">
                    <option value="0">Select</option>
                    <option value="1">1</option>
                    <option value="2">2</option>
                    <option value="3">3</option>
                   
                </select>
                <input type="hidden" name="dish_id" value="${dish['dish_id']}">
                    
              </td>
		</tr>
		`

	}
	table_create = `
	<table name = "myTable">
		<thead>
			<tr>
				<th>DishName</th>
				<th>DishPrice</th>
				<th>Quantity</th>
			</tr>
		</thead>
		<tbody>
			${table_body}
		</tbody>
		<input type = "hidden" name = "restuarant" value = "${rest_id}">
	</table>
	`
	$('#myModal.modal-body').html(table_create);
	$('$myModal').modal('show');

}

function OrderDishes(){
	table_create = documents.getElementsByName('myTable')[0];
	let xhr = new XMLHttpRequest();
	let url = 'order/';
	let dish = [];
	let restuarant = $(table_create.parentElement).find('input[name="rest_id"]').val();
	for(let i = 1; i < table_create.length; i++){
		row = table_elements.rows[i];

		quantity = parseInt(row.cells[3].getElementsByTagName('select')[0]);
		dish_id = row.cells[3].getElementsByTagName('input')[0].value;
		dish.push(
			'quantity':quantity,
			'dish_id' :dish_id,
			);
	}
	let result = {
		'dish':dish,
		'restuarant':restuarant,
	}
	result = JSON.stringyfy(result);
	
	xhr.open('POST', url, true);
	xhr.onload() = function(){
		alert("Your Order has been Placed");
	}
	xhttp.setRequestHeader('Content-Type', 'application/json');
	xhr.send(result);
}