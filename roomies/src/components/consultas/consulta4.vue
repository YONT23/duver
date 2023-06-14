<template>
    <center>
        <h1>Consulta N# 4</h1>
        <h1>Mostrando Consulta</h1>
    </center>
    <div class="alert alert-success" role="alert">
        <center>
            <p>Consulta con utilizacion de SQL para, para realizar la sigiente busquedad.
                &nbsp; "SELECT id, nombre, ciudad, correo FROM tbl_persona;"...</p>
            <button type="button" class="boton" onclick="history.back()">Volver</button>
            <br /><br />
                    <a position:left @click="descargarPdf()" class="boton">Reporte</a> 
        </center>
    </div>
    <div>
          <table class="table">
            <thead class="thead-light">
              <tr>
                <th scope="col">#</th>
                <th scope="col">Nombre</th>
                <th scope="col">Ciudad</th>
                <th scope="col">Correo</th>
              </tr>
            </thead>
            <tbody>
              <tr  v-for="c in cc" :key="c.id">
                <th scope="row">{{c.id}}</th>
                <td>{{c.nombre}}</td>
                <td>{{c.ciudad}}</td>
                <td>{{c.correo}}</td>
              </tr>
            </tbody>
          </table>
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
        axios.get('http://127.0.0.1:8000/inmueble/consulta4/').then(response => this.cc = response.data)
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