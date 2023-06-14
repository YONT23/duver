<template>
    <div class="card card-border-color card-border-color-primary w-75 mx-auto">
        <div class="card-header card-header-divider text-center fs-4">Registrar tus dependencias</div>
        <div class="card-body">
            <div class="form-group">
                <label for="nombre" class="form-label">Nombre</label>
                <input type="text" v-model="maestra.maes_nombre" id="nombre" class="form-control" required>
            </div>
            <div class="form-group">
                <label for="dependencia" class="form-label">Dependencia</label>
                <select name="dependencia" id="dependencia" v-model="maestra.maes_dependencia" class="form-select">
                    <option :value="''"></option>
                    <template v-for="dep in dependencia">
                        <option :value="dep['id']">{{dep['maes_nombre']}}</option>
                    </template>
                </select>
            </div>
            <div class="form-group">
                <label for="valor" class="form-label">Valor</label>
                <input type="number" v-model="maestra.maes_valor" id="valor" class="form-control" required>
            </div>
            <div class="form-group">
                <label for="estados" class="form-label">Estados</label>
                <input type="number" v-model="maestra.maes_estado" id="estados" class="form-control" required>
            </div>

            <div class="d-flex flex-row justify-content-around">
                <button class="btn btn-success w-25" @click="submitData(maestra)">Save</button>
                <router-link to="/inmueble/all/" class="btn btn-danger w-25">Cancel</router-link>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import { store } from "../context/store";

import axios from "axios";

const maestra = {
    maes_nombre: '',
    maes_dependencia: '',
    maes_valor: '',
    maes_estado: ''
};

export default {
    data() {
        return {
            maestra,
            dependencia: []
        }
    },
    methods: {
        submitData(maestra: any) {
            store.commit('saveMaestra', { url: 'http://localhost:8000/maestra/create/', data: maestra });
            this.$data.maestra = {
                maes_nombre: '',
                maes_dependencia: '',
                maes_valor: '',
                maes_estado: ''
            };
        }
    },
    async beforeMount() {

        const resp = await axios.post('http://localhost:8000/maestra/dependencias/', { dependencia: '' });
        this.$data.dependencia = resp.data;
    }
}

</script>

<style scoped>

</style>