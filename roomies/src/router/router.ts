import { createRouter, createWebHistory } from "vue-router";
import { RouteRecordRaw } from 'vue-router';
import { store } from "../context/store";
//Home
import inicio from '../components/home.vue';
//Consultas
import Consultas from '../components/consultas/consultas.vue';
import Consulta1 from '../components/consultas/consulta1.vue';
import Consulta2 from '../components/consultas/consulta2.vue';
import Consulta3 from '../components/consultas/consulta3.vue';
import Consulta4 from '../components/consultas/consulta4.vue';
import Consulta5 from '../components/consultas/consulta5.vue';
import Consulta6 from '../components/consultas/consulta6.vue';
//Servicios
const nuevos = () =>
  import("../components/servicios/nuevo.vue");

import Servicios from '../components/servicios/mostrarservicios.vue'
//Clientes
import Clientes from '../components/clientes/mostrarclientes.vue';
import nuevoc from '../components/clientes/nuevo.vue';
import editar from '../components/clientes/edit.vue';

const login = () => import("../components/auth/login.vue");
const register = () => import("../components/auth/registrarse.vue");
const maestra = () => import("../components/maestra.vue");

const routes: RouteRecordRaw[] = [
  //Register
  { path: "/nuevos", component: nuevos },
  { path: "/servicios", component: Servicios },
  //Home
  { path: "/home", component: inicio },
  //Personas
  { path: "/clientes", component: Clientes },
  { path: "/nuevoc", component: nuevoc, },
  { path: "/editarc", component: editar, },
  //Consultas
  { path: "/consultas", component: Consultas },
  { path: "/consulta1", component: Consulta1 },
  { path: "/consulta2", component: Consulta2 },
  { path: "/consulta3", component: Consulta3 },
  { path: "/consulta4", component: Consulta4 },
  { path: "/consulta5", component: Consulta5 },
  { path: "/consulta6", component: Consulta6 },
  //Servicios
  { path: "/servicios", component: Servicios },
  { path: "/nuevos", component: nuevos },
  //Login
  { path: "/auth/login/", component: login, name: "login", },
  { path: "/auth/register/", component: register, name: "register", },
  { path: '/maestra/', component: maestra, name: 'maestra' }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

router.beforeEach(async (to, from, next) => {
  const auth = JSON.parse(localStorage.getItem("auth")!);
  store.commit("saveToken", auth);
  if (
    to.name! !== "login" &&
    to.name !== "register" &&
    to.name !== "maestra" &&
    !store.state.isAuthenticate.auth
  ) {
    return next({ name: "login" });
  } else next();
});

export { router };