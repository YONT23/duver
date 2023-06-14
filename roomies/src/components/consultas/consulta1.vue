
<template>
    <div id="function" class="container">
        <center>
            <h1>Consulta N° 1</h1>
            <h1>Mostrando Consulta</h1>
        </center>
        <div class="row">
            <div class="alert alert-success" role="alert">
                <center>
                    <p>Mostrar todos los Clientes y la cantidad de hombres, como la de mujeres que hacen parte de
                        Roomies.</p>
                    <button type="button" class="boton" onclick="history.back()">Volver</button><br /><br />
                    <a position:left @click="descargarPdf()" class="boton">Reporte</a> 
                    <br />
                </center>
            </div>
            <table class="table table-hover">
                <thead>
                    <tr>
                        <th scope="col">Clientes Totales</th>
                        <th scope="col">Mujeres</th>
                        <th scope="col">Hombres</th>
                    </tr>
                </thead>
                <tbody>
                    <tr class="table-light">
                        <td>{{ c.clientes_totales }}</td>
                        <td>{{ c.clientes_mujeres }}</td>
                        <td>{{ c.clientes_hombres }}</td>
                        <td></td>
                    </tr>
                </tbody>
            </table>
            <div class="alert alert-dismissible alert-info" role="alert">
                Yonatha Mendoza || Roomies.
            </div>
        </div>
        <div class="col-1">

        </div>
    </div>
</template>


<script lang="ts">
import axios from 'axios'
import html2pdf from 'html2pdf.js'
export default {
    data() {
        return {
            c: []
        }
    },
    mounted() {
        axios.get('http://127.0.0.1:8000/inmueble/consulta1/').then(response => this.c = response.data)
    },
    methods: {
        descargarPdf() {
            var element = document.getElementById('element-to-pdf');
            var opt = {
                margin: 0.5,
                filename: 'roomiesPdf.pdf',
                image: { type: 'jpeg', quality: 0.98 },
                html2canvas: { scale: 3 },
                jsPDF: { unit: 'in', format: 'letter', orientation: 'portrait' }
            };
            html2pdf().from(element).set(opt).save();
        }
    },
}
</script>

<style scoped lang="css">
h1 {
    justify-content: center;
    justify-items: center;
    left: 60%;
}

.boton {
	background-color:#637aad;
	border-radius:28px;
	border:1px solid #314179;
	display:inline-block;
	cursor:pointer;
	color:#ffffff;
	font-family:Arial;
	font-size:19px;
	padding:6px 58px;
	text-decoration:none;
	text-shadow:0px 1px 0px #7a8eb9;
}
.boton:hover {
	background-color:#5972a7;
}
.boton:active {
	position:relative;
	top:1px;
}
</style>