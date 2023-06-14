<template>
    <div id="app">
        <div class="card card-border-color card-border-color-primary w-100 mx-auto">
            <div class="card-header card-header-divider text-center fs-4">PERSONAS
                <p class="lead">Tabla con las personas que hacen parte de Roomies.</p>
                <a position:left href="/nuevoc" class="agregar">Agregar</a>
                <br />
                <a position:left @click="descargarExcel()" class="agregar">Descargar Tabla</a> <br />
                <a position:left @click="descargarPdf()" class="agregar">Descargar Pdf</a> <br />
            </div>
            <table id="element-to-pdf" class="table">
                <thead>
                    <tr>
                        <th scoped="col">#</th>
                        <th scoped="col">Nombre</th>
                        <th scoped="col">Apellido</th>
                        <th scoped="col">Ciudad</th>
                        <th scoped="col">Correo</th>
                        <th scoped="col">Identidad</th>

                    </tr>
                </thead>
                <tbody>
                    <tr v-for="persona in personas" :key="persona.id">
                        <td scoped="row">{{ persona.id }}</td>
                        <td scoped="row">{{ persona.nombre }}</td>
                        <td scoped="row">{{ persona.apellido }}</td>
                        <td scoped="row">{{ persona.ciudad }}</td>
                        <td scoped="row">{{ persona.correo }}</td>
                        <td scoped="row">{{ persona.num_identidad }}</td>
                        <td scoped="row">
                            <p title="Eliminar"><a class="btn btn-danger btn-sm "
                                    v-on:click="deletePersona(persona.id)"><i class="bi bi-archive"></i></a></p>
                        </td>
                        <td scoped="row">
                            <p title="Actualizar"><a class="btn btn-info btn-sm "
                                    v-on:click="updatePersona(persona.id)"><i class="bi bi-arrow-down-up"></i></a></p>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>

<script lang="ts">
import axios from 'axios'
import exportXlsFile from 'export-from-json'
import html2pdf from 'html2pdf.js'

export default {
    data() {
        return {
            personas: [],
        }
    },
    mounted() {
        axios.get('http://127.0.0.1:8000/persona/').then(response => this.personas = response.data)
    },
    methods: {
        deletePersona(id) {
            const url = 'http://127.0.0.1:8000/persona/delete/' + id + '/';
            axios.delete(url).then(response => {
                this.personas;
                console.log(response);
                console.log('Borrado')
            })
                .catch(e => {
                    console.log(e, 'Error al eliminar')
                });
        },
        updatePersona(id) {
                this.$router.push('/editarc/' + id);
        },
        descargarExcel() {
            const data = this.personas;
            const fileName = 'excelRoomies';
            const exportType = exportXlsFile.types.xls
            exportXlsFile({ data, fileName, exportType })
        },
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
    }
}
</script>

<style scoped>
.center {
    justify-content: center;
    justify-items: center;
}

.table {
    border: 0.3ch;
    border-color: rgb(68, 78, 75);
    border-style: solid;
    font-weight: 500;
    margin: 0;
    padding: 2em;
    text-align: center;
    place-items: center;
}

.th {
    border: 0.2ch
}

.centrar {
    justify-content: center;
    justify-items: center;
}

.agregar {

    box-shadow: 0px 10px 14px -7px #276873;
    background: linear-gradient(to bottom, #599bb3 5%, #408c99 100%);
    background-color: #599bb3;
    border-radius: 8px;
    display: inline-block;
    cursor: pointer;
    color: #ffffff;
    font-family: Arial;
    font-size: 13px;
    font-weight: bold;
    padding: 4px 36px;
    text-decoration: none;
    text-shadow: 0px 1px 0px #3d768a;
}

.agregar:hover {
    background: linear-gradient(to bottom, #408c99 5%, #599bb3 100%);
    background-color: #408c99;
}

.agregar:active {
    position: relative;
    top: 1px;
}
</style>