
<template>
    <center>
        <h1>Consulta N# 3</h1>
        <h1>Mostrando Consulta</h1>
    </center>
    <div class="alert alert-success" role="alert">
        <center>
            <p>Mostrar Fecha de inicio precio y fecha final de los alquileres disponibles.</p>
            <button type="button" class="boton" onclick="history.back()">Volver</button>
            <br /><br />
                    <a position:left @click="descargarPdf()" class="boton">Reporte</a> 
        </center>
    </div>
    <div v-for="c in cc" :key="c.id">
        <div class="card">
            <ul class="list-group">
                <h5>Registro</h5>
                <li class="list-group-item">Fecha Inicio: {{ c.fecha_inicio }}</li>
                <li class="list-group-item">Precio: {{ c.precio }}</li>
                <li class="list-group-item">Fecha Final: {{ c.fecha_final }}</li>
            </ul>
        </div>
    </div>
</template>


<script  lang="ts">
import axios from 'axios'
import html2pdf from 'html2pdf.js'
export default {
    data() {
        return {
            cc: []
        }
    },
    mounted() {
        axios.get('http://127.0.0.1:8000/inmueble/consulta2/').then(response => this.cc = response.data)
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
.boton {
    background-color: #637aad;
    border-radius: 28px;
    border: 1px solid #314179;
    display: inline-block;
    cursor: pointer;
    color: #ffffff;
    font-family: Arial;
    font-size: 19px;
    padding: 6px 58px;
    text-decoration: none;
    text-shadow: 0px 1px 0px #7a8eb9;
}

.boton:hover {
    background-color: #5972a7;
}

.boton:active {
    position: relative;
    top: 1px;
}
</style>