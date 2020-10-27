// inicio de sesion 

window.onload = function(){

    const openModButton = document.querySelectorAll('[data-mod-target]')
    const closeModButton = document.querySelectorAll('[data-close-button]')
    const overlay = document.getElementById("overlay")

    openModButton.forEach(button => {
        button.addEventListener('click',() => {
            const modal = document.querySelector(button.dataset.modTarget)
            openModal(modal)
        })
    })

    overlay.addEventListener('click',() => {
        const modal = document.getElementById('mod')
        closeModal(modal)
    })

    closeModButton.forEach(button => {
        button.addEventListener('click', () => {
            const modal = button.closest('.mod')
            closeModal(modal)
        })
    })

    function openModal(modal){
        if (modal == null) {return}
        modal.classList.add('active')
        overlay.classList.add('active')
    }

    function closeModal(modal){
        
        if (modal == null) {return}
        modal.classList.remove('active')
        overlay.classList.remove('active')
    }
}
