$(document).ready(function () {
    $('#imprimir').DataTable({
        dom: 'Bfrtip',
        rowReorder: {
            selector: 'td:nth-child(2)'
        },
        responsive: true,

        buttons: [{
            extend: 'print',
            text: '<input type="submit" class="btn btn-success" value="imprimir"></button>',
            className: 'btn btn-success',
            exportOptions: {
                columns: ':not(:last-child)'
            }
        },

        ],
        "bDestroy": true,
        "language": {

            "lengthMenu": "Mostrar _MENU_ registros por página",
            "zeroRecords": "No se encontro registro",
            "info": "Mostrando página _PAGE_ de _PAGES_",
            "infoEmpty": "No hay registros disponibles",
            "search": "Buscar: ",
            "infoFiltered": "(filtrado de _MAX_ registros totales)",
            "paginate": {
                "next": "Siguiente",
                "previous": "Anterior"
            }
        }
    });
});