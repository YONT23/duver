<template>
    <div class="card card-border-color card-border-color-primary w-75 mx-auto">
        <div class="card-header card-header-divider text-center fs-4">Registrar tu servicio</div>
        <div class="card-body">
            <div class="form-group">
                <label for="ciudad" class="form-label">Ciudad</label>
                <input type="text" v-model="servicio.ciudad" id="ciudad" class="form-control" required>
            </div>
            <div class="form-group">
                <label for="estrato" class="form-label">Estrato</label>
                <input type="text" v-model="servicio.estrato" id="estrato" class="form-control" required>
            </div>
            <div class="form-group">
                <label for="num_pisos" class="form-label">Numero de pisos</label>
                <input type="number" v-model="servicio.num_pisos" id="num_pisos" class="form-control" required>
            </div>
            <div class="form-group">
                <label for="num_baños" class="form-label">Numero de baños</label>
                <input type="number" v-model="servicio.num_baños" id="num_baños" class="form-control" required>
            </div>
            <div class="form-group">
                <label for="num_habitaciones" class="form-label">Numero de habitaciones</label>
                <input type="number" v-model="servicio.num_habitaciones" id="num_habitaciones" class="form-control"
                    required>
            </div>
            <div class="form-group">
                <label for="superficie" class="form-label">Superficie</label>
                <input type="text" v-model="servicio.superficie" id="superficie" class="form-control" required>
            </div>
            <div class="form-group">
                <label for="descripcion" class="form-label">Descripcion</label>
                <input type="text" v-model="servicio.descripcion" id="descripcion" class="form-control" required>
            </div>
            <div class="d-flex flex-row justify-content-around">
                <button class="btn btn-success w-25" @click="submitData(servicio)">Guardar</button>
                <router-link to="/servicios" class="btn btn-danger w-25">Cancelar</router-link>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import { ServiciosI } from "../../models/servicios";
export default {
    props: {
        servicio: {
            type: Object as () => ServiciosI,
            required: true
        },
        submitData:{
            type: Function as ()=> any,
            
        }
    },
}
</script>

<style scoped>
.card-header {
    background-color: cornflowerblue;
}
</style>