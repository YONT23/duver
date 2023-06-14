<template>
    <form>
        <div class="card card-border-color card-border-color-primary w-75 mx-auto">
            <div class="card-header card-header-divider text-center fs-4">Llena el formulario de personas</div>
            <div class="card-body">
                <div class="form-group">
                    <label for="" class="form-label">Nombre</label>
                    <input type="text" v-model="newPersona.nombre" class="form-control" required>
                </div>
                <div class="form-group">
                    <label for="" class="form-label">Apellido</label>
                    <input type="text" v-model="newPersona.apellido" class="form-control" required>
                </div>
                <div class="form-group">
                    <label for="" class="form-label">Telefono</label>
                    <input type="text" v-model="newPersona.telefono" class="form-control" required>
                </div>
                <div class="form-group">
                    <label for="" class="form-label">Correo</label>
                    <input type="text" v-model="newPersona.correo" class="form-control" required>
                </div>
                <div class="form-group">
                    <label for="" class="form-label">Ciudad</label>
                    <input type="text" v-model="newPersona.ciudad" class="form-control" required>
                </div>
                <div class="form-group">
                    <label for="" class="form-label">Tipo Sexo</label>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    <select class="form-group" v-model="newPersona.tipo_sexo">
                        <option value selected>----------</option>
                        <option value="2">Masculino</option>
                        <option value="3">Femenino</option>
                    </select>
                </div>
                <div class="form-group">
                    <label for="" class="form-label">Identificacion</label>
                    <input type="text" v-model="newPersona.num_identidad" class="form-control" required>
                </div>
                <div class="form-group">
                    <label for="" class="form-label">Tipo de documento</label>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    <select class="form-group" v-model="newPersona.tipo_identificacion">
                        <option value selected>----------</option>
                        <option value="5">Cedula de Ciudadania</option>
                        <option value="6">Tarjeta de Identidad</option>
                    </select>
                </div>
                <div class="d-flex flex-row justify-content-around">
                    <a class="agregar" v-on:click="editar()">Actualizar</a>
                    <a onclick="history.back()" class="agregar">Volver</a>
                </div>
            </div>
        </div>

    </form>
</template>

<script  lang="ts">
import axios from 'axios'
export default {
    data() {
        return {
            personaId:null,
            newPersona:{
                nombre: '', apellido: '', telefono: '', correo: '',
                ciudad: '', num_identidad: '', tipo_sexo:'',tipo_identificacion:'' 
            }
        }
    },
    methods: {
        editar(){
            axios.put('http://127.0.0.1:8000/persona/update/', this.newPersona)
            .then(data =>{
                console.log(data)
            })
        }
    },
    mounted() {
        this.personaId = this.$route.params.id;
        axios.get('http://127.0.0.1:8000/persona/' + this.personaId)
            .then(datos => {
                this.newPersona.nombre = datos.data[0].nombre;
                this.newPersona.apellido = datos.data[0].apellido;
                this.newPersona.telefono = datos.data[0].telefono;
                this.newPersona.correo = datos.data[0].correo;
                this.newPersona.ciudad = datos.data[0].ciudad;
                this.newPersona.tipo_sexo = datos.data[0].tipo_sexo;
                this.newPersona.num_identidad = datos.data[0].num_identidad;
                this.newPersona.tipo_identificacion = datos.data[0].tipo_identificacion;
                console.log(this.newPersona);
            })
    }
}
</script>

<style scoped>
.card-header {
    background-color: cornflowerblue;
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