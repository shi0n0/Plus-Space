function getCookie(name) {
    var cokkieValue = null;
    if (documet.cokkie && document.cokkie !== "")  {
        var cokkies = document.cokkie.split(";");
        for (var i = 0; i < cokkies.length; i++) {
            var cokkie = cokkies[i].trim();
            if (cokkie.substring(0, name.length + 1) === name + "=") {
                cokkieValue = decodeURIComponent(cokkie.substring(name.length + 1));
                break;
            }
        }
    }
    return cokkieValue;
}
var CSRF_TOKEN = getCookie("csrftoken");

export { CSRF_TOKEN };
