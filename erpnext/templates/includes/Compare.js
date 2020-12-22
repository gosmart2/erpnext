$(document).ready(function(){
	$("#btn-login").click(function(){
		frappe.freeze();
			frappe.call({
				type: "POST",
				method: "erpnext.templates.pages.Compare.create_data",
				args: {
					doc:"hello",
				},
				btn: this,
				callback: function(r){
					frappe.unfreeze();
					if(r.message){
 	 		var myjson=r.message;

 	 		 var col = [];
        	for (var i = 0; i < myjson.length; i++) {
            for (var key in myjson[i]) {
                if (col.indexOf(key) === -1) {
                    col.push(key);
                }
            }
        }
        var myTableDiv = document.getElementById("myText");
        var table = document.createElement("table");
        table.style="font-family:Times New Roman;border-collapse:collapse; border:1px solid black;";
        // Create table header row using the extracted headers above.
        var tr = table.insertRow(-1);                   // table row.

        for (var i = 0; i < col.length; i++) {
            var th = document.createElement("th");  
            th.style="font-family:Times New Roman;border-collapse:collapse; border:1px solid black; text-align:center;";
            th.innerHTML = col[i];
            tr.appendChild(th);
        }

        // add json data to the table as rows.
        for (var i = 0; i < myjson.length; i++) {

            tr = table.insertRow(-1);

            for (var j = 0; j < col.length; j++) {
                var tabCell = tr.insertCell(-1);
                 tabCell.style="font-family:Times New Roman;border-collapse:collapse; border:1px solid black;";
                tabCell.innerHTML = myjson[i][col[j]];
            }
        }
        myTableDiv.appendChild(table);

        var sumVal=0;
        for(var i = 1; i < table.rows.length; i++)
            {
            sumVal = sumVal + parseInt(table.rows[i].cells[4].innerHTML);
            }
            document.getElementById("val").innerHTML = "Sum Value = " + sumVal;
    //  document.getElementById("val2").innerHTML = "Max Value = "+maxVal;  
     // document.getElementById("val3").innerHTML = "Min Value = "+minVal;   
			}
			}
			});
	});
});