var data = "/static/data/comunas_mas_grandes.json";
var visualization = d3plus.viz()
.container("#comunas_mas_grandes_10000hab")
.data(data)
.type("bar")
.width(false)
.height(500)
.resize(true)
.id(["pos","comuna"])
.x("comuna")
.y("encuentros_10000hab")
.color(function(d){
      return d.encuentros_10000hab > 0 ? "#3689a3":"#3689a3";
    })
.depth(1)
.format({
  "text": function(text, params) {
    if (text === "poblacion") {
      return "Población";
    }
    if (text === "encuentros") {
      return "Encuentros locales";
    }    
    if (text === "encuentros_10000hab") {
      return "Encuentros locales por cada 10.000 habitantes";
    }
    if (text === "idh") {
      return "Índice de Desarrollo Humano";
    }
    else {
      return d3plus.string.title(text, params);
    }
  },
  "number": function(number, params) {
    var myLocale = {
      "decimal": ",",
      "thousands": ".",
      "grouping": [3],
      "currency": ["$", ""],
      "dateTime": "%a %b %e %X %Y",
      "date": "%m/%d/%Y",
      "time": "%H:%M:%S",
      "periods": ["AM", "PM"],
      "days": ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
      "shortDays": ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"],
      "months": ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"],
      "shortMonths": ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
    };
    var localeFormatter = d3.locale(myLocale);
    var numberFormat = localeFormatter.numberFormat(",.2r");
    var formatted = d3plus.number.format(number, params);
      if (params.key === "encuentros") {
        return numberFormat(number);
      }
      if (params.key === "poblacion") {
        return numberFormat(number);
      }
      else {
        return formatted;
      }
  },
  "locale": "es_ES"
})
.font({"family": "Roboto"})
.title("Encuentros locales por comuna por cada 10.000 habitantes (20 valores más altos)")
//.title({"sub": "Divisiones de acuerdo al número de encuentros por cada 10.000 habitantes por zona geográfica"})
.tooltip(["encuentros"])
.tooltip({"share": false})
/*.labels({"align": "left", "valign": "top"})*/
.legend(false)
.messages({"branding":true})
.order(function(d) {
    return ["Maipú","Puente Alto","La Florida","Antofagasta ","Viña del Mar","Talca","Puerto Montt","Temuco","La Serena","Arica","Valdivia","Concepción","Iquique","Valparaíso ","Las Condes","Recoleta","La Reina","Ñuñoa","Providencia","Santiago"].indexOf(d.comuna);
})
.draw();