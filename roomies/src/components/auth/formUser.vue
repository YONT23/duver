<template>
    <div class="card card-border-color card-border-color-primary w-75 mx-auto">
        <div class="card-header card-header-divider text-center fs-4">Registro</div>
        <div class="card-body">
            <div class="form-group">
                <label for="nombre" class="form-label">Nombre</label>
                <input type="text" v-model="persona.nombre" id="nombre" class="form-control" required>
            </div>
            <div class="form-group">
                <label for="apellido" class="form-label">Apellido</label>
                <input type="text" v-model="persona.apellido" id="apellido" class="form-control" required>
            </div>
            <div class="form-group">
                <label for="telefono" class="form-label">Telefono</label>
                <input type="text" v-model="persona.telefono" id="telefono" class="form-control" required>
            </div>
            <div class="form-group">
                <label for="email" class="form-label">Correo</label>
                <input type="email" v-model="persona.correo" id="email" class="form-control" required>
            </div>
            <div class="form-group">
                <label for="ciudad" class="form-label">Ciudad</label>
                <input type="text" v-model="persona.ciudad" id="ciudad" class="form-control" required>
            </div>
            <div class="form-group">
                <label for="tipo_iden" class="form-label">Tipo identificacion</label>
                <select name="tipo_iden" id="tipo_iden" v-model="persona.tipo_identificacion">
                    <template v-for="i in persona.tipo_identificacion">
                        <option :value="i['id']">{{i['maes_nombre']}}</option>
                    </template>
                </select>
            </div>
            <div class="form-group">
                <label for="num_iden" class="form-label">Identificacion</label>
                <input type="text" v-model="persona.Identificacion" id="num_iden" class="form-control" required>
            </div>
            <div class="form-group">
                <label for="username" class="form-label">Usenamer</label>
                <input type="text" v-model="usuario.username" id="username" class="form-control" required>
            </div>
            <div class="form-group">
                <label for="password" class="form-label">Password</label>
                <input type="password" v-model="usuario.password" id="password" class="form-control" required>
            </div>
            <div class="form-group">
                <label for="salario" class="form-label">Salario</label>
                <input type="number" v-model="usuario.salario" id="salario" class="form-control" required>
            </div>
            <div class="form-group">
                <label for="empleo" class="form-label">Empleo</label>
                <input type="text" v-model="usuario.empleo" id="empleo" class="form-control" required>
            </div>
            <div class="d-flex flex-row justify-content-around">
                <button class="btn btn-success w-25" @click="submitData({persona,usuario})">Save</button>
                <router-link to="/inmueble/all/" class="btn btn-danger w-25">Cancel</router-link>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import { PersonasI, Iusuario } from '../../models/personas';
export default {
    props: {
        persona: {
            type: Object as () => PersonasI,
            required: true
        },
        usuario: {
            type: Object as () => Iusuario,
            required: true
        },
        submitData: {
            type: Function as () => any,

        }
    },
}
</script>