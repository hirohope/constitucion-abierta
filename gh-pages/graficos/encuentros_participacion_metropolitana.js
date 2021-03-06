var visualization = d3plus.viz()
.container("#encuentros_participacion_metropolitana")
.data("graficos/encuentros_participacion_metropolitana.json")
.type("scatter")
.width(false)
.height(500)
.resize(true)
.id(["comuna"])
.size("poblacion")
.x("encuentros_10000hab")
.y("indice_participacion")
.color("color")
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
    if (text === "indice_participacion") {
      return "Porcentaje de participación";
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
      if (params.key === "encuentros_10000hab") {
        return numberFormat(number);
      }
      if (params.key === "poblacion") {
        return numberFormat(number);
      }
      if (params.key === "indice_participacion") {
        return numberFormat(number) + '%';
      }
      else {
        return formatted;
      }
  },
  "locale": "es_ES"
})
.font({"family": "Roboto"})
.title("Encuentros locales versus participación en elecciones municipales de la Región Metropolitana")
/*.title({"sub":"Considerando comunas con población de más de 10.000 habitantes"})*/
.tooltip(["encuentros_10000hab"])
.tooltip({"share": false})
.legend(false)
.messages({"branding":true})
.aggs({"idh":"mean","encuentros_10000hab":"mean"})
.draw();