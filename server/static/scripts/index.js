function ChangeColor() {
    let body = document.querySelector('body')
    let cards = document.querySelectorAll('.card')
    let card_comment = document.querySelector('#card_comment')
    let links = document.querySelectorAll('.link-for-js')
    let nav = document.querySelector('.navbar')
    let button_in_card = document.querySelectorAll('.btn_card')
    let form_control = document.querySelectorAll('.form-control')
    let buttons = document.querySelectorAll('.btn_site')

    if (nav.classList.contains("nav_my_css_dark")) {
        nav.classList.remove("nav_my_css_dark")
        nav.classList.add("nav_my_css_light")

    } else {
        nav.classList.remove("nav_my_css_light")
        nav.classList.add("nav_my_css_dark")
    }

    if (body.classList.contains("text-bg-dark")) {
        body.classList.remove("text-bg-dark")
        body.classList.add("text-bg-light")

    } else {
        body.classList.remove("text-bg-light")
        body.classList.add("text-bg-dark")
    }

    for (let index = 0; index < cards.length; ++index) {
        if (cards[index].classList.contains("text-bg-light")) {
            cards[index].classList.remove("text-bg-light")
            cards[index].classList.add("text-bg-dark")

        } else {
            cards[index].classList.remove("text-bg-dark")
            cards[index].classList.add("text-bg-light")
        }
    }

    for (let index = 0; index < button_in_card.length; ++index) {
        if (button_in_card[index].classList.contains("btn-dark")) {
            button_in_card[index].classList.remove("btn-dark")
            button_in_card[index].classList.add("btn-light")

        } else {
            button_in_card[index].classList.remove("btn-light")
            button_in_card[index].classList.add("btn-dark")
        }
    }

    for (let index = 0; index < form_control.length; ++index) {
        if (form_control[index].classList.contains("text-bg-light")) {
            form_control[index].classList.remove("text-bg-light")
            form_control[index].classList.add("text-bg-dark")

        } else {
            form_control[index].classList.remove("text-bg-dark")
            form_control[index].classList.add("text-bg-light")
        }
    }
    for (let index = 0; index < buttons.length; ++index) {
        if (buttons[index].classList.contains("btn-dark")) {
            buttons[index].classList.remove("btn-dark")
            buttons[index].classList.add("btn-light")

        } else {
            buttons[index].classList.remove("btn-light")
            buttons[index].classList.add("btn-dark")
        }
    }
    for (let index = 0; index < links.length; ++index) {
        if (links[index].classList.contains("link-dark")) {
            links[index].classList.remove("link-dark")
            links[index].classList.add("link-light")

        } else {
            links[index].classList.remove("link-light")
            links[index].classList.add("link-dark")
        }
    }

}


Button = document.querySelector('#flexSwitchCheckChecked')
Button.addEventListener('click', ChangeColor)

function changeFunction() {
    document.myform.submit();
}




