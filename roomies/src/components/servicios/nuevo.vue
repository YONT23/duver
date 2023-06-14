<template>
    <edit :servicio="servicio" :submit-data="submitData" />
</template>

<script lang="ts">
import { ServiciosI } from "../../models/servicios";
import edit from "./edit.vue";
import { store } from "../../context/store";


const servicio: ServiciosI = {
    serv_internet: '',
    serv_cocina: '',
    serv_patio: '',
    serv_ubicacion: '',
    habitacion: 0,
    huesped: 0,
    baño: 0,
    disponibilidad: 0,
};

export default {
    data() {
        return {
            servicio: servicio
        }
    },
    methods: {
        submitData(servicio: ServiciosI) {
            store.commit('postServicio', { ...this.$data.servicio, ...servicio });
        }
    },
    components: {
        edit
    }
}

</script>

<style scoped >


</style>