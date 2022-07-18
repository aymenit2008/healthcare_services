frappe.provide('hs.PivotRpf');
/*
var jQueryDatatableStyle = document.createElement("link");
jQueryDatatableStyle.rel = 'stylesheet';
jQueryDatatableStyle.type = "text/css";
jQueryDatatableStyle.href = "https://cdn.datatables.net/1.10.20/css/jquery.dataTables.min.css";
jQueryDatatableStyle.onload = function(){
	console.log("jQuery Datatable Style Loaded");
};
document.head.appendChild(jQueryDatatableStyle);
*/
$.getScript("/assets/healthcare_services/js/pivotjs/jquery-ui.min.js", function () {
	alert('Ready');

});
frappe.pages['pivot_rpf'].on_page_load = function(wrapper) {

	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'None',
		single_column: true
	});

	var profileclass = hs.PivotRpf.class;
	profileclass.setup(wrapper);
	profileclass.addfilters();
	$(wrapper).bind("show", () => {
		profileclass.refresh();
	});
}

hs.PivotRpf.class = {
	addfilters: function () {
		var rpfpage = this;
		this.fields = {};
		let date = this.page.add_field({
			label: "من تاريخ ",
			fieldname: "date",
			fieldtype: "Date",
			default: frappe.datetime.get_today()

		});
		let date2 = this.page.add_field({
			label: "الى تاريخ ",
			fieldname: "date",
			fieldtype: "Date",
			default: frappe.datetime.get_today()

		});
		let search = this.page.add_field({
			label: "بحث",
			fieldname: "search",
			fieldtype: "Button",
			click() {
				rpfpage.changeHtml(date.get_value(),date2.get_value());

			},
		});
		/*
		let print = this.page.add_field({
			label: "Print",
			fieldname: "print",
			fieldtype: "Button",
			click() {
				rpfpage.printDiv('.pvtRendererArea');

			},
		});
		*/

	},
	setup: function (wrapper, filters) {
		this.page = frappe.ui.make_app_page({
			parent: wrapper,
			title: __('Pivot Report'),
			single_column: true
		});
		this.wrapper = $(wrapper);
		this.main_section = this.wrapper.find(".layout-main-section");
		this.page.set_title("Pivot Report");
		this.page.clear_fields();
		//frappe.breadcrumbs.add("Credence");
		this.main_section.append(`<div id="trip_profile" class="row trip_profile "> <div id="trip_result" class="trip_result col-sm-12" style="    overflow: scroll;"> </div>  </div>`);
		this.$components_wrapper = this.wrapper.find('#trip_result');
		//this.$filter_wrapper = this.wrapper.find('.filter_trip');
	},
	refresh : function(){
		//alert('refresh page');
		alert("hiiii");
		this.$components_wrapper.html("");
		//this.$filter_wrapper.html("");
	},
	changeHtml:function(date,date2){
		var trippage = this;
		var data_rpf;
		//alert("date: s_cite:"+ page);

                var derivers = $.pivotUtilities.derivers;
                var renderers = $.extend($.pivotUtilities.renderers);

                var tpl = $.pivotUtilities.aggregatorTemplates;
                var sum = $.pivotUtilities.aggregatorTemplates.sum;
                var numberFormat = $.pivotUtilities.numberFormat;
                var intFormat = numberFormat({
                    digitsAfterDecimal: 0
                });

		frappe.call({
			// notypetrip ,fromdate, todate
			method: "healthcare_services.healthcare_services.page.pivot_rpf.pivot_rpf.pivot_rpf_q",
			async: false,
			args: {
				date: date,
				date2: date2
			},
			callback: function(r) {
				//alert(r.message['car']);
				if (!r.exc && r.message['data_rpf']) {
					data_rpf = r.message['data_rpf']
				}


			}
		});
		this.$components_wrapper.pivotUI(data_rpf, {
			rows: ["facility_name", "date"],
			cols: ["ser_name"],
			renderers: renderers,
			rendererName: "Table",
			//rendererName: "Horizontal Stacked Bar Chart",
			aggregatorName: "Integer Sum",
			vals: ["ser_no"],
			aggregator: sum(intFormat)(["ser_no"]),

			 // sorters: {
			 // 	"الحركة": $.pivotUtilities.sortAs(
			 // 		["رصيد سابق", "وارد", "منصرف", "الرصيد"]),
			 // 	Age: function(a, b) {
			 // 		return b - a;
			 // 	}
			 // }

		});





	},
	printDiv:function(elem){
		var mywindow = window.open('','Print-Window');
		var content = $(elem).html();
		var realContent = document.body.innerHTML;
		mywindow.document.open();
		mywindow.document.write('<html><body onload="window.print()">'+content+'</body></html>');
		//mywindow.document.close(); // necessary for IE >= 10

		mywindow.focus(); // necessary for IE >= 10*/
		mywindow.print();
		setTimeout(function(){mywindow.close();},10000);
		//document.body.innerHTML = realContent;
		//mywindow.close();
		return true;

	}

}