<template>
    <div class="card card-border-color card-border-color-primary w-100 mx-auto">
        <div>
            <div class="card w-80 mx-auto">
                <div class="card-body text-center">
                    <h2 class="fs-2">Servicios</h2>
                    <p class="lead">Servicios disponibles en Roomies.</p>
                    <a position:left href="/nuevos" class="agregar">Agregar</a>
                </div>
            </div>
        </div>
    </div>
    <div class="d-flex flex-row flex-wrap justify-content-around my-5">
        <div class="card card-transition" style="max-width: 20rem;cursor: pointer; " v-for="i in is" :key="i.id">
            <div class="card mb-3">
                <h3 class="card-header">Servicio: {{ i.id }}</h3>
                <div class="card-body">
                    <h5 class="card-title">{{ (i as any)?.pais_id.maes_nombre }} - {{ i.ciudad }}</h5>   &nbsp;
                 <center>
                    &nbsp;<h6 class="card-subtitle text-muted">Estrato: {{ i.estrato }}</h6>
                 </center>
                </div>
                <img class="card-img-top" :src="i.url_imagenes" alt="Image">
                <div class="card-body">
                    <p class="card-text">Las encuestas a los clietes que han ocupado esta propiedad concuerdan en la descripcion de que este inmuebles es: {{ i.descripcion }}</p>
                </div>
                <ul class="list-group list-group-flush">
                    <li class="list-group-item">Superficie: 
                        {{ i.superficie }}</li>
                    <li class="list-group-item"> Baños:
                        {{ i.num_baños }}</li>
                    <li class="list-group-item">Habitaciones:
                        {{ i.num_habitaciones }}</li>
                </ul>
            </div>
        </div>
    </div>
</template>

<script  lang="ts">
import axios from 'axios'

export default {
    data() {
        return {
            is: []
        }
    },
    mounted() {
        axios.get('http://127.0.0.1:8000/inmueble/').then(response => this.is = response.data)
    }
}
</script>

<style scoped lang="css">
.hijo {
    justify-content: center;
    left: 800px;
    top: 50%;

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

.card-pinned-top-end {
    position: relative;
    top: -10.1rem;
    right: -0.3rem;
}
</style>