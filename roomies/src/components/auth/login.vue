<template>
    <div class="card card-border-color card-border-color-primary w-70 mx-auto">
        <section class="vh-100" style="">
            <div class="container py-1 h-50">
                <div class="row d-flex justify-content-center align-items-center h-100">
                    <div class="col-12 col-md-1 col-lg-3 col-xl-5">
                        <div class="card shadow-2-strong" style="border-radius: 1rem;">
                            <div class="card-body p-4 text-center">
                                <h3 class="mb-3">Registro</h3>
                                <div class="form-outline mb-1">
                                    <input type="username" v-model="usuario.username" id="username"
                                        class="form-control form-control-lg" required />
                                    <label class="form-label" for="username">Username</label>
                                </div>
                                <div class="form-outline mb-1">
                                    <input type="password" v-model="usuario.password" id="password"
                                        class="form-control form-control-lg" required />
                                    <label class="form-label" for="password">Password</label>
                                </div>
                                <!-- Checkbox -->
                                <div class="form-check d-flex justify-content-start mb-1">
                                    <input class="form-check-input" type="checkbox" value="" id="form1Example3" />
                                    <label class="form-check-label" for="form1Example3"> Remember password </label>
                                </div>
                                <button class="btn btn-primary btn-lg btn-block" type="submit"
                                    @click="submitData(usuario)"><i class="fa-regular fa-registered"></i>
                                    Entrar</button>
                                <router-link to="/home" class="btn btn-lg btn-block btn-primary"
                                    style="background-color: #dd4b39;" type="submit"><i class="fa-solid fa-ban"></i>
                                    Cancelar</router-link>
                                <hr class="my-4">
                                <router-link class="btn btn-lg btn-block btn-primary mb-2" type="submit"
                                    style="background-color: #3b5998;" to="/auth/register/">
                                    Registrarse
                                </router-link>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </div>
</template>


<script scope lang="ts">

import { store } from "../../context/store";

const usuario = {
    username: '',
    password: ''
}

export default {
    data() {
        return {
            usuario
        }
    },
    methods: {
        submitData(data: any) {
            store.commit('authLogin', data);
        }
    }
}
</script>


<style>

</style>