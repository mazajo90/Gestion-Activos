const btnsEliminacion = document.querySelectorAll('.btnEliminacion')

function alert_creation_product(){
    $.confirm({
        theme: 'supervan',
        title: '',
        icon: 'fa fa-info',
        content: '¿Estas seguro de crear un articulo?',
        columnClass: 'medium',
        typeAnimated: true,
        cancelButtonClass: 'btn-primary',
        draggable: true,
        dragWindowBorder: false,
        buttons: {
            info: {
                text: "Si",
                btnClass: 'btn-green',
                action: function () {
                    
                }
            },
            danger: {
                text: "No",
                btnClass: 'btn-red',
                action: function () {
                    window.history.back();
                }
            },
        }
    })
}


