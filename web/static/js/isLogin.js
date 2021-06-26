window.onload = function () {
    var logoutGambiarra = document.getElementById('titulo').innerText;
   

    if (logoutGambiarra === 'Home') {
        document.getElementById('logout').style.display = 'inline';
        document.getElementById('services').style.display = 'inline';
    }
}