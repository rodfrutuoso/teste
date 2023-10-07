function toggleMode() {
    const html = document.documentElement;

    // if (html.classList.contains('light')){
    //     html.classList.remove('light')
    // } else {
    //     html.classList.add('light')
    // }
    html.classList.toggle('light')

    // Mudar imagem
    const img = document.querySelector("#profile img")

    if (html.classList.contains('light')) {
        img.setAttribute("src","./assets/euFoto.png")
    } else {
        img.setAttribute("src","./assets/eu3.png")
    }


}