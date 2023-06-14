<template>
    <div>
        <edit :servicio="servicio" :submit-data="submitData" />
    </div>
</template>

<script lang="ts">
import { } from "vue-router";
import { ServiciosI } from "../../models/servicios";
import edit from "./edit.vue";
import { store } from "../../context/store";
import axios from "axios";
const servicio: ServiciosI = {
    ciudad: '',
    descripcion: '',
    estrato: '',
    latitud: '0',
    longitud: '0',
    num_baños: 0,
    num_habitaciones: 0,
    num_pisos: 0,
    pais: 'Colombia',
    superficie: '',
    tipo_estado: '',
    tipo_inmueble: '',
    url_imagenes: "https://res.cloudinary.com/ddzkz3ijj/image/upload/v1665342976/descarga.jpg",
};
export default {
    data() {
        return {
            servicio: servicio
        }
    },
    methods: {
        submitData(servicio: ServiciosI) {
            store.commit('putInmueble', { url: "http://localhost:8000/inmueble/update/" + this.$route.params.id + '/', data: servicio });
            this.$router.push('/servicios');
        },
        async deleteInmueble(id: any) {
            const tokrn = store.getters.getToken;
            await axios.delete('http://localhost:8000/inmueble/delete/' + id,{headers:{
                Authorization:'Bearer ' + tokrn
            }});
            this.$router.push('/servicios');
        }
    },
    mounted() {
        this.$data.servicio = store.state.servicioOwner.find((inm) => inm.id === Number(this.$route.params.id))!;
    },
    components: {
        edit
    }
}
</script>

<style>
</style>